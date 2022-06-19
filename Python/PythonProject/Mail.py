import smtplib



message=""" From: Pooja Das <Poojadas2014.pd@gmail.com>
To: Rebhu  josh <rebhujj@gmail.com>
Subject:  What I find interesting on you?

Dear Rebhu,
    Hey! if you are reading this mail tht sure You receive my mail (Coding test kar rahi thi re).

    Ok so ya Why I finding Intersest on u , Well you r ere person coz of whom i am doing this ,You are the person Who tell me.That Pooja make ur identity.
    Tere world mere around nhi hona chahiye .Tera khud ka bhi world hona chahiye.

    And ya mjko daru peena na .
    bus thatz over

    regards,
    Pooja Das 
    (Last mai tjse Shaadi karugi re..)


"""
try:
    # Creates SMTP(Simple Mail Transport Protocol) session
    s=smtplib.SMTP('smtp.gmail.com', 587)#465,587

    # Start TLS(Transport Leyer Security ) for security


    s.starttls()

    # Authentication

    s.login("Poojadas2014.pd@gmail.com","hlbadhgdcvueqtxr")

    # Message to be sent



    # Sending the mail

   
    s.sendmail("Poojadas2014.pd@gmail.com","rebhujj@gmail.com",message)

    # Terminating the session
    s.quit()

    print("Mail Send Successfully")

except Exception as e:

    print("Error: unable to send email")
    print(str(e))