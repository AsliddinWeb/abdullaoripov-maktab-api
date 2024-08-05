from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TelegramBot, Message
from .serializers import MessageSerializer
from .utils import send_message

def get_latest_single_instance(model):
    return model.objects.last()


class SendMessageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            phone = serializer.validated_data['phone']
            message = serializer.validated_data['message']

            send_text = (f"✅ <b>Yangi xabar:</b>\n\n"
                         f"🙂<b>Ism: </b>{name}\n"
                         f"📞 <b>Telefon raqami: </b>{phone}\n"
                         f"🔖 <b>Xabar: </b>{message}")

            telegram_bot = TelegramBot.objects.last()
            if telegram_bot:
                for i in telegram_bot.admins.split(", "):
                    send_message(
                        token=telegram_bot.token,
                        chat_id=i,
                        text=send_text
                    )

            new_message = Message(**serializer.validated_data)
            new_message.save()

            return Response({'status': "Xabar yuborildi!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
