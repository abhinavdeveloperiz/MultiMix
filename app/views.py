from django.shortcuts import render,redirect
from app.models import Home,Gallery
from app.forms import Contact
# Create your views here.


def Home_view(request):
    qs=Home.objects.first()
    return render(request,'home.html',{"image":qs})

def Aboutus_view(Request):
    return render(Request,'about.html')

def Service_view(Request):
    return render(Request,'service.html')

def Gallery_view(request):
    qs=Gallery.objects.all()
    return render(request,'gallery.html',{"image":qs})

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def Contact_view(Request):
    if Request.method == "POST":
        form = Contact(Request.POST)
        if form.is_valid():
            instance = form.save()

            subject = f"New Enquiry: {instance.subject}"
            from_mail = settings.DEFAULT_FROM_EMAIL
            to_mail = [settings.DEFAULT_TO_EMAIL]

            # Plain text fallback
            plain_message = (
                f"You have received a new enquiry:\n\n"
                f"Name: {instance.name}\n"
                f"Phone: {instance.phone}\n"
                f"Subject: {instance.subject}\n"
                f"Message:\n{instance.message}"
            )

            # HTML message
            html_message = f"""
<table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f0f2f5; padding: 40px 0;">
  <tr>
    <td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.08); padding: 30px; font-family: 'Segoe UI', Roboto, sans-serif;">
        <tr>
          <td align="center" style="padding-bottom: 20px;">
            <h1 style="margin: 0; color: #2c3e50;">📩 New Enquiry Received</h1>
            <p style="color: #888; margin-top: 5px;">You have a new message from your website</p>
          </td>
        </tr>
        <tr>
          <td>
            <table width="100%" style="font-size: 16px; color: #333;">
              <tr>
                <td style="padding: 10px 0;"><strong>Name:</strong></td>
                <td style="padding: 10px 0;">{instance.name}</td>
              </tr>
              <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px 0;"><strong>Phone:</strong></td>
                <td style="padding: 10px 0;">{instance.phone}</td>
              </tr>
              <tr>
                <td style="padding: 10px 0;"><strong>Subject:</strong></td>
                <td style="padding: 10px 0;">{instance.subject}</td>
              </tr>
              <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px 0; vertical-align: top;"><strong>Message:</strong></td>
                <td style="padding: 10px 0;">{instance.message}</td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding-top: 30px;">
            <p style="font-size: 12px; color: #aaa;">This email was automatically sent from your website's contact form.</p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
"""


            send_mail(
                subject,
                plain_message,
                from_mail,
                to_mail,
                fail_silently=False,
                html_message=html_message 
            )

            messages.success(Request, "Your enquiry has been submitted successfully.")
            return redirect("contact")
    else:
        form = Contact()

    return render(Request, 'contact.html', {"form": form})



    
