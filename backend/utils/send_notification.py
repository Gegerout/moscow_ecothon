import requests  # Импортируем библиотеку для выполнения HTTP-запросов


def send_notification(body, title):
    # URL для отправки уведомлений через Firebase Cloud Messaging (FCM)
    url = 'https://fcm.googleapis.com/v1/projects/ecoproject-6568c/messages:send'

    # Данные для отправки уведомления, включающие сообщение и заголовок
    data = {
        "message": {
            "token": "cX-6e-9DRjyBGslMV4usFD:APA91bHjX70B4fiFQztGHR19Gp_wW9Ry2FhQmqb6W9qq_ZxKsfDp7ccpi9kLgXe7J91zAbe_dxlAk53q8Zdwef-TIE3EJaP0jfIWjRiYejLVR5BmVGZmIG_W278cnVUHGTWAoaz5IZYw",  # Токен устройства, на которое будет отправлено уведомление
            "notification": {
                "body": body,  # Тело уведомления
                "title": title  # Заголовок уведомления
            }
        }
    }

    # Отправляем POST-запрос с данными уведомления и заголовком для авторизации
    response = requests.post(url, json=data, headers={
        "Authorization": "Bearer ya29.a0AcM612xU7BzQkHanMV1xcDL24kCQGBxvs6YIAbDFDbxhtBATZ42PAjcEw6MjEYS-Dw3aab_AHxnTLwNnVw0Op6cufWYTQZg-ItRoSx2OjYIBsktsXlVMGh7a2SPSlzZ1nWwZIy0NoaM_7WZiL4T46ZhtJY6aYt0svYc-jw-yaCgYKAZQSARMSFQHGX2MiN6ANUir3fUrMSWyxF2HQwA0175"
    })

    # Проверяем статус-код ответа от сервера
    if response.status_code == 200:
        return True  # Успешная отправка уведомления
    else:
        return False  # Ошибка при отправке