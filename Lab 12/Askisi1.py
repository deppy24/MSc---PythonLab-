'''Γράψτε ένα πρόγραμμα με χρήση του προτύπου WSGI,
 όπου θα επιστρέφει το κείμενο που θα διαβάσει από ένα αρχείο κει
'''

def application(environ, start_response):
    # Ορίστε τον τύπο περιεχομένου
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    # Διαβάστε το περιεχόμενο από το αρχείο κειμένου
    try:
        with open('textfile.txt', 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        # Αν υπάρχει σφάλμα κατά την ανάγνωση του αρχείου
        content = f"Error reading file: {str(e)}"

    return [content.encode('utf-8')]

