

class Task:
    def __init__(self):
        pass

    def produce_links(self, json_file):
        pass

    def requests_data(self, links):
        pass

    @staticmethod
    def save_to_file(file_name, content):
        with open(file_name, 'w') as f:
            f.write(content)

    def process_data(self, file_name):
        pass

    def requests_all_data(self):
        pass

    def clear(self):
        pass
