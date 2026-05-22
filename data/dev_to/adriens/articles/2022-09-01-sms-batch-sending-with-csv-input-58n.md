---
comments: 3
id: 1176356
is_dev_challenge: false
published_at: '2022-09-01T20:41:53Z'
reactions: 5
reading_time_minutes: 1
tags:
- showdev
- news
- java
- ux
title: 🚚 SMS batch sending with csv input
url: https://dev.to/optnc/sms-batch-sending-with-csv-input-58n
---

## ❔ About

In many customer usecases, people need to **send SMS in a batch mode... for a very wide amount of business cases.**

## 💭 ERP Integration considerations and `csv`

Customer data can be managed through an endless list of ERP/CRM and middlewares (relational databases, ETL jobs,...), including hand-made solutions and Spreadsheets, etc...

☝️ Still, at some point, they all may need to **notify their customers on a regular or event driven basis** (birthdays, fidelity points, special events, emergency, dates,...).

What all these people do is an export of : 

1️⃣ The customer phone number
2️⃣ The custom message to send

This is exactly what this feature is about.

We need to send that data to your customer thanks to a simple `csv` as :

☑️ They are easy to produce on **any language and any platform/middleware**
☑️ There are a lot of **ready to use automation tools** (Power Automate, Zapier, IFTTT,...) around them

## 🗃️ Input data : the `csv`

The input can come from any spreadsheet : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7fxgqrdnmg6c7eok0hjt.png)

... then exported to `csv` :

```
to,message
+687XXXXXX,"Hey Jack, All work and no play makes Jack a dull boy."
+687XXXXXX,"Today is your birthday, come to our shop to enjoy your discount."
+687XXXXXX,"Come enjoy black friday tomorrow morning!"
+687XXXXXX,"Yoy now have 1000pts. on your fidelity card, come enjoy discount today"
+687XXXXXX,"Your command has been delivered and awaits for you at the postoffice"
```

Next, to send the `csv`, just : 

```csv
opt-sms send -f "${SHORT_NUMBER_CODE}"\
    -c "${ACCOUNT}"\
    -i "~/demo_batch_sms.csv"
```

And you're done.

Now... enough talk, let's enjoy the demo!


## 🍿 Demo

{% youtube qjjETvi0W9k %}