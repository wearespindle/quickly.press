import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

import messagebird

from quickly.buttons.models import EmergencyButtonClient
from quickly.families.models import FamilyMember
from quickly.schedules.models import Schedule


class PanicGet(APIView):
    """
    A custom endpoint for GET request.
    """
    def get(self, request, format=None):
        """
        Send a message via MessagBird and return the status.
        """
        reciepient = []
        user = EmergencyButtonClient.objects.first()
        current_time = datetime.datetime.now().time()
        family_members = FamilyMember.objects.filter(emergency_button_client=user)
        schedules = Schedule.objects.filter(family_member__in=family_members,
                                            start__lte=current_time,
                                            end__gte=current_time)
        for schedule in schedules:
            reciepient.append(schedule.family_member.phone_number)

        api_token = 'RTDWFuAIoGzINuBTRDl5uDOiO'
        client = messagebird.Client(api_token)

        message = client.message_create(
            'MessageBird',
            reciepient,
            'panic ... Panic ... PANIC',
            {'reference' : 'quicklypress'},
        )

        voice_message = client.voice_message_create(
            '+31614665916',
            'Panic, panic, panic',
            {'language' : 'en-gb', 'voice': 'female' },
        )
        return Response({"success": True, "content": "Panic message sent."})
