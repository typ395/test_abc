import yaml
class YamlOperation:
    def __init__(self,locator_file):
        with open(locator_file) as yaml_file:
            self.data=yaml.load(yaml_file,yaml.FullLoader)
    def get_locator(self,page,local):
        return self.data[page][local]
# if __name__ == '__main__':
#     y=YamlOperation('D:\\测试\\selenium\\复习\\cry_sys\\conifg\\test.yaml')
#     print(y.get_locator('LoginPage','username'))