# Asset Request Bot

## Project Overview

Asset Request Bot is a Telegram chatbot that helps employees request company assets such as laptops, monitors, and software licenses.

Instead of filling forms or sending emails, employees can simply chat with the bot. The bot collects the required information, validates the employee against HR data, and stores the request in a database.

---

## Problem Statement

In many organizations, requesting assets involves multiple manual steps and approvals, which can be time-consuming.

This project simplifies the process by automating asset requests through a chatbot.

---

## How It Works

1. Employee starts the bot.
2. Bot asks a series of questions:
   - Employee ID
   - Asset Type
   - Asset Name
   - Business Justification
3. Employee details are validated using HRIS data.
4. A structured asset request is created.
5. The request is saved in SQLite database.
6. Requests can be viewed using the `/requests` command.

---

## Features

- Telegram-based chatbot
- Slot-filling conversation flow
- Employee validation using HRIS data
- Asset request generation
- SQLite database storage
- View submitted requests

---

## Technology Used

- Python
- Telegram Bot API
- SQLite Database
- JSON (Mock HRIS Data)
- python-telegram-bot

---

## Project Structure

```text
asset-request-bot/
│
├── bot.py
├── agent.py
├── validation.py
├── database.py
├── data/
│   └── employees.json
└── db/
    └── asset_requests.db
```

---

## Example

### User

```text
/start
```

### Bot

```text
Please enter your Employee ID
```

### User

```text
EMP1001
```

### Bot

```text
What type of asset do you need?
```

### User

```text
Laptop
```

### Bot

```text
Please specify the asset name/model
```

### User

```text
Dell Latitude 5440
```

### Bot

```text
Please provide the business justification
```

### User

```text
New project onboarding
```

### Bot

```text
Request Saved Successfully
```

---

## Sample Request Stored

```json
{
  "request_id": "AR-C9888B33",
  "employee_id": "EMP1001",
  "asset_type": "Laptop",
  "asset_name": "Dell Latitude 5440",
  "justification": "New project onboarding",
  "status": "Submitted"
}
```

---

## Expected Outcome

- Faster asset request process
- Reduced manual work
- Better tracking of requests
- Centralized storage using SQLite

---

## Conclusion

This project demonstrates how a conversational AI bot can automate the asset request process by collecting user requirements, validating employee information, and storing requests in a structured format.