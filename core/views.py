from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from urllib.parse import urlparse, parse_qs
from .models import Account


# UI
def home(request):
    return render(request, "index.html")


# ✅ SAVE QR → DB
@csrf_exempt
def save_qr(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=400)

    data = json.loads(request.body)
    uri = data.get("data")

    if not uri:
        return JsonResponse({"error": "No QR data"}, status=400)

    parsed = urlparse(uri)
    params = parse_qs(parsed.query)

    # clean secret
    raw_secret = params.get("secret", [""])[0]
    secret = raw_secret.replace(" ", "").upper()

    issuer = params.get("issuer", ["Unknown"])[0]
    name = parsed.path[1:] if parsed.path else "Unknown"

    acc = Account.objects.create(
        name=name,
        issuer=issuer,
        secret=secret
    )

    # ✅ IMPORTANT: return saved object
    return JsonResponse({
        "id": acc.id,
        "name": acc.name,
        "issuer": acc.issuer,
        "secret": acc.secret
    })


# ✅ GET ALL ACCOUNTS
def get_accounts(request):
    accounts = Account.objects.all().values("id", "name", "issuer", "secret")
    return JsonResponse(list(accounts), safe=False)


# ✅ DELETE
@csrf_exempt
def delete_account(request, id):
    if request.method == "POST":
        Account.objects.filter(id=id).delete()
        return JsonResponse({"status": "deleted"})

    return JsonResponse({"error": "Invalid method"}, status=400)