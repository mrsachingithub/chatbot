import re
import operator
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load conversation data
QA_DATA = {}
CSV_FILENAME = os.getenv("CSV_FILENAME", "Conversation.csv")
TXT_FILENAME = os.getenv("TXT_FILENAME", "conversation.txt")

CSV_PATH = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
TXT_PATH = os.path.join(os.path.dirname(__file__), TXT_FILENAME)

def load_data():
    global QA_DATA
    
    # 1. Load CSV
    if os.path.exists(CSV_PATH):
        try:
            with open(CSV_PATH, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None) # Skip header
                for row in reader:
                    if len(row) >= 3:
                        question = row[1].strip().lower()
                        answer = row[2].strip()
                        QA_DATA[question] = answer
        except Exception as e:
            print(f"Error loading CSV: {e}")

    # 2. Load TXT (Python list format)
    if os.path.exists(TXT_PATH):
        try:
            with open(TXT_PATH, mode='r', encoding='utf-8') as f:
                content = f.read()
                # Simple parsing for ['Q', 'A'] pattern
                # We'll look for: ['question', 'answer']
                # Be careful with quotes inside.
                # Regex approach: Pattern finding ['(.*?)', '(.*?)'] roughly
                # Or simplistic manual parsing if regex is tricky with nested quotes.
                # Given the file format is standard python list of lists:
                # Let's use ast.literal_eval for safety if it's valid python syntax
                import ast
                # Extract the list part: source= [...]
                start_index = content.find('[')
                if start_index != -1:
                    list_content = content[start_index:]
                    try:
                        data_list = ast.literal_eval(list_content)
                        for pair in data_list:
                            if len(pair) >= 2:
                                q = str(pair[0]).strip().lower()
                                a = str(pair[1]).strip()
                                QA_DATA[q] = a
                    except Exception as parse_err:
                        print(f"Error parsing TXT content: {parse_err}")
                        
        except Exception as e:
            print(f"Error loading TXT: {e}")

# Initial load
load_data()

def process_query(message: str) -> str:
    """
    Process the user message and return a response.
    Includes basic arithmetic capabilities and CSV-based QA.
    """
    message_lower = message.strip().lower()
    
    # 1. Try CSV Match first (Exact or simple containment)
    if message_lower in QA_DATA:
        return QA_DATA[message_lower]
    
    # Fuzzy match/Partial match from CSV?
    # Simple iteration for now: if user query is very similar
    for q, a in QA_DATA.items():
        if q in message_lower or message_lower in q:
            # Prevent very short matches like "i" matching "hi"
            if len(q) > 3 and len(message_lower) > 3:
                return a
    
    # 2. Try Math
    math_result = evaluate_math(message)
    if math_result:
        return math_result
    
    # 3. Hardcoded Fallbacks
    if "hello" in message_lower or "hi" in message_lower:
        return "Hello! How can I help you today?"
    elif "time" in message_lower:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "name" in message_lower:
        return "I am a simple chatbot with math and QA skills."
    else:
        return f"I received your message: '{message}'. I'm still learning!"

def evaluate_math(message: str) -> str:
    """
    Extract and evaluate simple math expressions.
    Supports: +, -, *, /
    Example inputs: "5 + 5", "calculate 10 * 2", "what is 100 / 10"
    """
    # Regex to find two numbers separated by an operator
    # \d+(\.\d+)? matches integers or decimals
    # \s* matches optional whitespace
    # [\+\-\*\/] matches the operator
    pattern = r"(\d+(?:\.\d+)?)\s*([\+\-\*\/])\s*(\d+(?:\.\d+)?)"
    match = re.search(pattern, message)
    
    if match:
        num1 = float(match.group(1))
        op_symbol = match.group(2)
        num2 = float(match.group(3))
        
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        
        try:
            op_func = ops.get(op_symbol)
            if op_func:
                result = op_func(num1, num2)
                # Format integer results as integers
                if result.is_integer():
                    result = int(result)
                return f"The result is {result}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception:
            return "I couldn't calculate that."
            
    return None

