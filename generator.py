#!/usr/bin/env python
import json
import re

class Generator:
        def sanitize(self, pattern):
                return re.sub("'", "\\'", pattern)

class Nginx(Generator):
        template = """if ($http_user_agent ~* '{pattern}') {{\n  return 404;\n}}"""

        def generate(self, pattern):
                sanitized = self.sanitize(pattern)
                print(self.template.format(pattern = sanitized))

if __name__ == '__main__':
        with open("crawler-user-agents.json") as f:
                content = f.read()

        crawlers = json.loads(content)
        generator = Nginx()
        for crawler in crawlers:
                pattern = crawler['pattern']
                generator.generate(pattern)
        

        
