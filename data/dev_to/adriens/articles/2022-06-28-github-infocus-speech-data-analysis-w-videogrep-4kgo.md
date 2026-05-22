---
comments: 3
id: 1109713
is_dev_challenge: false
published_at: '2022-06-28T06:47:57Z'
reactions: 1
reading_time_minutes: 3
tags:
- datascience
- fun
- devops
- github
title: 📊 "GitHub InFocus" speech data analysis w. videogrep 🎞️
url: https://dev.to/adriens/github-infocus-speech-data-analysis-w-videogrep-4kgo
---

## 🙋 About

GitHub recently published _"Propelling your DevOps to new heights | GitHub InFocus"_, a exciting DevOPS related content : 

{% youtube https://youtu.be/awQ7LFxfXWE %}

Also, within the same period of time I watched an episode of ["The Download" series](https://youtube.com/playlist?list=PL0lo9MOBetEE0goMLEl97vO7slruNVj43) (animated by [`@film_girl`](https://twitter.com/film_girl) ):

{% embed https://youtu.be/FdkSTzp_NTY?t=271 %}

This episode did introduce `videogrep` : 

{% github antiboredom/videogrep %}

Then came the idea : 

> _What if I was analyzing "GitHub Infocus" with `videogrep` ?_

This short post will guide through this first trial on videogrep and what I have been able to produce, discover... and the fun I also had.

☝️ Notice that I used the following excellent tutorial to perform this experience 👇


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8h2zzg3d70vq95xa8tl2.png)
](https://lav.io/notes/videogrep-tutorial/) 

## 📥 Get the video with `yt-dlp`

First I want to get the YT video `https://youtu.be/awQ7LFxfXWE
` locally, therefore you can choose many encoding options and choose the one that best fits your needs (`-F` option) but in our case, we'll get the default one :

```
yt-dlp https://youtu.be/awQ7LFxfXWE -o propelling_your_devops.mp4 --write-auto-sub
```

Then you are ready for the next step : use `videogrep`.

## 📊 Text analysis with `ngrams`

`videogrep` makes it possible (and super easy) to analyze text within the (downloaded `vtt` files) subtitles.

So, what are the trendiest group of word ( called `ngrams`) in the video ? Let's find out !

While the single word analysis is not really interesting : 

```
❯ videogrep --input propelling_your_devops.mp4.webm --ngrams 1 | head -10
to 449
and 352
that 347
you 323
the 322
we 306
a 255
of 251
so 167
is 157
```

2-`ngrams` are much more **interesting about the underlying intents of the video** : 

```
❯ videogrep --input propelling_your_devops.mp4.webm --ngrams 2 | head -7
want to 97
that we 61
you can 55
you know 54
going to 51
we have 45
we can 45
```

... soon confirmed with the 3-`grams` : 

```
❯ videogrep --input propelling_your_devops.mp4.webm --ngrams 3 | head -9
we want to 30
you want to 20
a lot of 19
want to make 19
make sure that 18
i'm going to 17
to make sure 17
we have a 16
i want to 13
```

## 🔬 Short analysis

With the help of `ngrams`, within less than a second we discover, by grepping the text of the video that 

> _"GitHub focuses it attention on what they want... and also on **what you want to achieve... and make**"_

👉 **That first fact already tells us a lot.**

☝️ It also puts in evidence 

> _"the inclusive approach while using a lot of "I" and "We"_

... which is also pretty exciting to **onboard us on the product they are showcasing** ❣️

## ✂️🎞️ Cut & get shorts

Now, the fun part.

You have made a text analysis but... wouldn't it be fun to see the movie of these grepped terms ?...


⚠️ **Spoiler alert : Yes it is ❕ (and it's easy)** 🤣

These are called `fragments`. Let's get some of them.

## 🎯 The "Want" movie

Let's get all the sentences containing "want"

```
videogrep --input propelling_your_devops.mp4.webm --search 'want' --resyncsubs 0.1 --output want_sentence.mp4
```

{% youtube qzmH5TUjMS4 %}

🤪 **Also "we want" to get the "want" movie** 🤣 :

```
videogrep --input propelling_your_devops.mp4.webm --search 'we want to' --search-type fragment --resyncsubs 0.1 --output want.mp4
```

{% youtube kQoupAbMJHo %}

## 🤓 GH talking about code

What we think the more when we think about Github services is : the "code".

Let's make them talk about "code"

```
videogrep --input propelling_your_devops.mp4.webm --search 'code' --search-type fragment --resyncsubs 0.1 --output code.mp4
```

{% youtube M_nHtbR7zJU %}

## ➰ Github about GitHub 😹

Last but not least, I'd love to 

> _see how GitHub talks about GitHub_

```
videogrep --input propelling_your_devops.mp4.webm --search 'github' --search-type fragment --resyncsubs 0.1 --output github.mp4
```

{% youtube JFN9at7Eg8w %}

## 🧑‍🎨 Conclusion

These tools open a very wide area for speech and video analysis... making it possible to put in evidence patterns, intentions or simply have fun.

Also, being aware that `yt-dlp` makes it possbible to download complete channel, playlists or search queries... 

> **_possibilities are endless._**

## 🔖 Resources

- [`Vosk`](https://alphacephei.com/vosk/) : _speech recognition toolkit_
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) : _A `youtube-dl` fork with additional features and fixes_
- [`@sam_lavigne`](https://twitter.com/sam_lavigne)
- ["GitHub Infocus 2022 analysis" playlist on YT](https://youtube.com/playlist?list=PLVaySOddZPMfWhV0Zr8BHpXVOLDKBMDqu)

## 🗞️ News

In its [`2.1.1`](https://github.com/antiboredom/videogrep/releases/tag/2.1.1) , `videogrep` adds some really cool features like (but not only) : 

- Finding "non-english vtt subtitle files"
- "Examples that integrate with [spaCy](https://spacy.io/)"