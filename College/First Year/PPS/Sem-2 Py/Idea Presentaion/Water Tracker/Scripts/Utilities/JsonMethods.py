import os, json
def save_data(self, data):
    try:
        if not os.path.exists(self.Assets):
            os.makedirs(self.Assets)
        with open(self.json_mode_file, 'w') as file:
            json.dump(data, file, indent=1)
        self.logger.info("Data saved successfully.")
    except Exception as e:
        self.logger.error(f"Error saving data: {e}")

def load_data_mode(self, mode):
    try:
        if not os.path.exists(self.json_mode_file):
            self.logger.info("Data file does not exist. Creating and saving default data.")
            save_data(self=self, data={"mode": mode})
        with open(self.json_mode_file, 'r') as file:
            return json.load(file)
    except Exception as e:
        self.logger.error(f"Error loading data: {e}")
        return {}