---
comments: 9
id: 1180998
is_dev_challenge: false
published_at: '2022-09-12T20:14:00Z'
reactions: 0
reading_time_minutes: 2
tags: []
title: ☎️ An Open Source Java SDK to validate phonenumbers in New-Caledonia 🧑‍🤝‍🧑
url: https://dev.to/optnc/an-open-source-java-sdk-to-validate-phonenumbers-in-new-caledonia-pkl
---

## ❔ About

Recenlty we saw a very nice & interesting Discussion landing on our [`opt-nc` Github Organization](https://github.com/opt-nc) : 


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5j76qiha1j6al8xii5gz.png)](https://github.com/orgs/opt-nc/discussions/13)

With a very well explained use case :

> _"Bonjour, disposer d'un SDK voire d'une API permettant de valider des numéros de téléphone ou encore de détecter si un numéro est un numéro de fixe ou un numéro de mobile."_

> _"Avec ces outils, il serait possible facilement d'améliorer la qualité de bases de données ou encore rendre des formulaires web plus efficaces."_

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f4gr0wh3xp5sz7nxwd7z.png)](https://github.com/orgs/opt-nc/discussions/13)

Quite rapidly we discovered that it could help a lot of people enhancing the data quality of Information Systems... and even ours !

This first intro post is dedicated to announce the release of the SDK.

## 😎 Open source repo

Here is the repo :

{% github opt-nc/phonenumber-validator %}

##  🚀 Get started

[Add SDK to your repo](https://github.com/opt-nc/phonenumber-validator#-maven), then :

```java
System.out.println("Type de numéro : " + PhoneNumberValidator.getPhoneType("+687514243").name());
System.out.println("Mobile ? : " + (PhoneNumberValidator.isMobile("+687514243") ? "oui" : "non"));
System.out.println("Fixe ? : " + (PhoneNumberValidator.isFixe("+687514243") ? "oui" : "non"));
System.out.println("Special ? : " + (PhoneNumberValidator.isSpecial("+687514243") ? "oui" : "non"));
```

## 🛡️ Security

As dependencies are monitored and code security is enabled, you can safely analyze code and see if any toxic code is embedded in the SDK :

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j5btmqhte6b11tlhflr2.png)](https://github.com/opt-nc/phonenumber-validator/security/code-scanning)

## ➰ Feedbacks

Feel free to send feedback by :

🎫 [Dropping an issue](https://github.com/opt-nc/phonenumber-validator/issues)
🧑‍🤝‍🧑 [Opening or participating to a discussion](https://github.com/opt-nc/phonenumber-validator/discussions)
🎁 [SDK delivery](https://github.com/orgs/opt-nc/discussions/13#discussioncomment-3629378) for [#ProgrammersDay](https://twitter.com/hashtag/ProgrammersDay) 🤓