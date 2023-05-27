from rest_framework.decorators import api_view
from rest_framework.response import Response
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pickle4 import pickle
# Create your views here.

@api_view(["GET"])
def Home(request):
    end_point_list={
        "GoogleCalendarInitView":"/rest/v1/calendar/init/",
        "GoogleCalendarRedirectView":"/rest/v1/calendar/redirect/"
    }
    return Response({"EndPoint List":end_point_list})

@api_view(["GET"])
def GoogleCalendarInitView(request):
    try:
        scopes=['https://www.googleapis.com/auth/calendar']
        flow = InstalledAppFlow.from_client_secrets_file(
                    '././client_secret.json', scopes=scopes)
        
        creds = flow.run_local_server()
        
        # Save the credentials for the next run
        pickle.dump(creds, open('token.pkl',"wb"))

        return Response({"ok"})
    except:
        return Response({"failed!"})

@api_view(["GET"])
def GoogleCalendarRedirectView(request):
    try:
        creds=pickle.load(open("././token.pkl","rb"))
        print(creds)
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        print('Getting the list of events')
        calendar_result = service.calendarList().list().execute()
        calendar_id = calendar_result["items"][0]["id"]
        events_result = service.events().list(calendarId=calendar_id).execute()
        # print(events_result["items"][0])
        return Response(events_result["items"])
    except:
        return Response({"failed!"})