class Config:

    def __init__(self, configAbsPath):
        self.config = {}

        with open(configAbsPath, 'r') as _file:
            lines = _file.readlines()

            for line in lines:
                var, value = line.split('=')
                
                parsedVar = self._parse(var)
                parsedValue = self._parse(value)
                self.config[parsedVar] = parsedValue


    def _remove_whitespace(self, string):
        chars = [' ', '\n', '\r']

        for char in chars:
            string = string.replace(char, '')

        return string


    def _remove_quotes(self, string):
        chars = ['"', '\'']

        for char in chars:
            string = string.replace(char, '')

        return string


    def _parse(self, string):
        string = self._remove_whitespace(string)
        string = self._remove_quotes(string)

        return string


    def __getattr__(self, attr):
        return self.config[attr]

