import uuid
from slot_manager import SlotManager
from validation import validate_employee, is_asset_allowed


class AssetRequestAgent:
    def __init__(self):
        self.slot_manager = SlotManager()

    def process_input(self, user_input):
        current_slot = self.slot_manager.get_next_missing_slot()

        if current_slot:
            self.slot_manager.update_slot(current_slot, user_input)

        # Validate employee immediately after employee_id is entered
        if current_slot == "employee_id":
            valid, employee = validate_employee(user_input)

            if not valid:
                self.slot_manager.update_slot("employee_id", None)
                return "❌ Employee ID not found. Please enter a valid Employee ID."

        # Ask next question
        next_slot = self.slot_manager.get_next_missing_slot()

        if next_slot:
            return self.slot_manager.get_slot_question(next_slot)

        # All slots collected
        return self.generate_request()

    def start_conversation(self):
        return self.slot_manager.get_slot_question("employee_id")

    def generate_request(self):
        data = self.slot_manager.get_data()

        valid, employee = validate_employee(data["employee_id"])

        if not is_asset_allowed(employee, data["asset_type"]):
            return "❌ You are not eligible for this asset."

        request_data = {
            "request_id": f"AR-{str(uuid.uuid4())[:8].upper()}",
            "employee_id": data["employee_id"],
            "asset_type": data["asset_type"],
            "asset_name": data["asset_name"],
            "justification": data["justification"],
            "status": "Submitted"
        }

        return request_data


if __name__ == "__main__":
    agent = AssetRequestAgent()

    print(agent.start_conversation())

    while True:
        user_input = input("> ")

        result = agent.process_input(user_input)

        print(result)

        if isinstance(result, dict):
            break