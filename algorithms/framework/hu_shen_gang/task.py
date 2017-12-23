

class Task:
    def produce_links(self, json_file):
        pass

    def requests_data(self, links):
        pass

    def save_to_file(self, file_name, content):
        with open(file_name, 'w') as f:
            f.write(content)

    def process_data(self, file_name):
        pass

    def requests_all_data(self):
        pass

    def clear():
        pass
