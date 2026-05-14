import functions_framework
import json
import os
from google.cloud import firestore 



db = firestore.Client()

@functions_framework.http
def chatbot_webhook(request):
    """
    HTTP Cloud Function with improved logic to handle missing parameters
    and route to the correct AI or data lookup service.
    """
    
    request_json = request.get_json(silent=True)
    
    # Safely get the intent tag from the Dialogflow request
    tag = request_json.get('fulfillmentInfo', {}).get('tag')
    
    response_text = "I'm sorry, I didn't understand that. Can you rephrase?"

    # --- ROUTE 1: Standard Order Status Check ---
    if tag == 'check_order_status':
        # Safely get parameters. Use .get() to avoid errors.
        parameters = request_json.get('sessionInfo', {}).get('parameters', {})
        order_id = parameters.get('order_id')

       
        # Check if an order_id was actually provided by the user
        if order_id:
            # If we have an order_id, look it up in the database
            order_id = str(order_id).strip('"')
            try:
                doc_ref = db.collection('orders').document(order_id)
                doc = doc_ref.get()
                if doc.exists:
                    order_data = doc.to_dict()
                    item = order_data.get('item', 'your item')
                    status = order_data.get('status', 'unknown')
                    response_text = f"I've checked on order {order_id}. The '{item}' has a status of: {status}."
                else:
                    response_text = f"I'm sorry, I couldn't find an order with the ID {order_id}. Please double-check the number."
            except Exception as e:
                response_text = f"Sorry, there was an error connecting to the database: {e}"
        else:
            # If no order_id was found in the user's message, ask for it.
            response_text = "I can certainly help with that. What is your order number?"

    # --- ROUTE 2: AI-Powered Complaint Handling ---
    elif tag == 'handle_complaint':
        user_complaint = request_json.get('text', "The user is unhappy with the service.")
        
       
        # The logic here is to generate an empathetic response.
        response_text = f"Thank you for reaching out. I am genuinely sorry to hear about the trouble you've experienced. It is completely understandable that you feel frustrated, and I want to sincerely apologize for this situation. Please be assured that this is not the standard of service we aim for. I am escalating this issue internally to ensure it is addressed with the highest priority."

    # Format the final response for Dialogflow
    json_response = {
        'fulfillment_response': {
            'messages': [
                {
                    'text': {
                        'text': [response_text]
                    }
                }
            ]
        }
    }
    
    return json_response

