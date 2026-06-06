class SlotManager:
    REQUIRED_SLOTS = [
        "employee_id",
        "asset_type",
        "asset_name",
        "justification"
    ]

    def __init__(self):
        self.slots = {
            "employee_id": None,
            "asset_type": None,
            "asset_name": None,
            "justification": None
        }

    def update_slot(self, slot_name, value):
        if slot_name in self.slots:
            self.slots[slot_name] = value

    def get_missing_slots(self):
        return [
            slot for slot, value in self.slots.items()
            if value is None
        ]

    def is_complete(self):
        return len(self.get_missing_slots()) == 0

    def get_next_missing_slot(self):
        missing = self.get_missing_slots()
        return missing[0] if missing else None

    def get_slot_question(self, slot):
        questions = {
            "employee_id": "Please enter your Employee ID:",
            "asset_type": "What type of asset do you need? (Laptop, License, Monitor, etc.)",
            "asset_name": "Please specify the asset name/model:",
            "justification": "Please provide the business justification:"
        }

        return questions.get(slot, "Please provide the required information.")

    def get_data(self):
        return self.slots


if __name__ == "__main__":
    manager = SlotManager()

    print("Missing:", manager.get_missing_slots())

    manager.update_slot("employee_id", "EMP1001")

    print("Missing:", manager.get_missing_slots())

    print("Next Question:")
    print(manager.get_slot_question(manager.get_next_missing_slot()))