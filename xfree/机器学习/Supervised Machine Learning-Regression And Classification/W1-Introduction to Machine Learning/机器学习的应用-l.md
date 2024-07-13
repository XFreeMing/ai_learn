WEBVTT

1
00:00:01.190 --> 00:00:03.660
In this class, you'll learn about
> 在这门课程中，你将学习

2
00:00:03.660 --> 00:00:05.190
the state of the art and also
> 最前沿的技术，还将

3
00:00:05.190 --> 00:00:06.480
practice implementing
> 实践实现

4
00:00:06.480 --> 00:00:08.830
machine learning
algorithms yourself.
> 机器学习算法。

5
00:00:08.830 --> 00:00:10.290
You'll learn about the most
> 你将学习最重要的

6
00:00:10.290 --> 00:00:12.180
important machine
learning algorithms,
> 机器学习算法，

7
00:00:12.180 --> 00:00:13.920
some of which are exactly
> 其中一些正是
8
00:00:13.920 --> 00:00:15.720
what's being used in large AI or
> 大型AI公司正在使用的

9
00:00:15.720 --> 00:00:18.385
large tech companies
today and you
> 今天的技术公司，你

10
00:00:18.385 --> 00:00:21.780
get a sense of what is the
state of the art in AI.
> 了解到AI的最新技术。

11
00:00:21.780 --> 00:00:25.590
Beyond learning the algorithms
though, in this class,
> 除了学习算法之外，在这门课程中，

12
00:00:25.590 --> 00:00:28.470
you'll also learn all the
important practical tips
> 你还将学习所有重要的实用技巧

13
00:00:28.470 --> 00:00:31.170
and tricks for making
them perform well.
> 和窍门，使它们表现良好。

14
00:00:31.170 --> 00:00:33.090
You get to implement
them and see
> 你将实现它们并看到

15
00:00:33.090 --> 00:00:35.665
how they work for yourself.
> 它们是如何工作的。

16
00:00:35.665 --> 00:00:39.665
Why is machine learning
so widely used today?
> 为什么机器学习今天如此广泛使用？

17
00:00:39.665 --> 00:00:41.750
Machine Learning had grown up as
> 机器学习作为一个领域已经成熟

18
00:00:41.750 --> 00:00:45.020
a sub-field of AI or
artificial intelligence.
> 作为人工智能的一个子领域。

19
00:00:45.020 --> 00:00:47.350
We wanted to build
intelligent machines.
> 我们想要构建智能机器。

20
00:00:47.350 --> 00:00:48.860
It turns out that there are
> 结果表明，有一些


21
00:00:48.860 --> 00:00:51.560
a few basic things that we
could program a machine to do,
> 我们可以编写程序让机器做一些基本的事情，

22
00:00:51.560 --> 00:00:54.305
such as how to find the
shortest path from a to b,
> 比如如何从a到b找到最短路径，

23
00:00:54.305 --> 00:00:55.810
like in your GPS.
> 就像在你的GPS中一样。

24
00:00:55.810 --> 00:00:59.255
But for the most part, we just
did not know how to write
> 但在大多数情况下，我们不知道如何编写

25
00:00:59.255 --> 00:01:01.130
an explicit program to
> 一个明确的程序来

26
00:01:01.130 --> 00:01:02.915
do many of the more
interesting things,
> 做许多更有趣的事情，

27
00:01:02.915 --> 00:01:04.910
such as perform web search,
> 比如执行网络搜索，

28
00:01:04.910 --> 00:01:07.010
recognize human speech, diagnose
> 识别人类语音，诊断

29
00:01:07.010 --> 00:01:10.060
diseases from X-rays or
build a self-driving car.
> 从X光片中诊断疾病或制造自动驾驶汽车。

30
00:01:10.060 --> 00:01:13.565
The only way we knew
how to do these things
> 我们唯一知道如何做这些事情的方法

31
00:01:13.565 --> 00:01:17.545
was to have a machine
learn to do it by itself.
> 是让机器自己学会做。

32
00:01:17.545 --> 00:01:19.820
For me, when I founded
> 对我来说，当我创立

33
00:01:19.820 --> 00:01:21.890
and was leading the
Google Brain Team,
> 并领导谷歌大脑团队时，

34
00:01:21.890 --> 00:01:24.395
I worked on problems
like speech recognition,
> 我解决了诸如语音识别之类的问题，

35
00:01:24.395 --> 00:01:26.030
computer vision for Google Maps,
> 为Google地图的计算机视觉，

36
00:01:26.030 --> 00:01:28.550
Street View images
and advertising,
> 街景图像和广告，

37
00:01:28.550 --> 00:01:30.620
or leading AI Baidu,
> 或领导百度AI，

38
00:01:30.620 --> 00:01:34.025
I worked on everything from
AI for augmented reality
> 我做了从增强现实的AI

39
00:01:34.025 --> 00:01:35.915
to combating payment fraud
> 到打击支付欺诈

40
00:01:35.915 --> 00:01:38.245
to leading a
self-driving car team.
> 到领导自动驾驶汽车团队。

41
00:01:38.245 --> 00:01:40.830
Most recently, at landing.AI,
> 最近，在landing.AI，

42
00:01:40.830 --> 00:01:42.950
AI Fund and
Stanford University,
> AI基金和斯坦福大学，

43
00:01:42.950 --> 00:01:45.530
I'm beginning to work on AI
applications in the factory,
> 我开始在工厂中研究AI应用，

44
00:01:45.530 --> 00:01:47.915
large-scale agriculture,
health care,
> 大规模农业，医疗保健，

45
00:01:47.915 --> 00:01:49.985
e-commerce, and other problems.
> 电子商务和其他问题。

46
00:01:49.985 --> 00:01:52.280
Today, there are
hundreds of thousands,
> 今天，有数十万人，
47
00:01:52.280 --> 00:01:53.555
perhaps millions of people
> 也许有数百万人

48
00:01:53.555 --> 00:01:55.460
working on machine
learning applications who
> 在从事机器学习应用的人

49
00:01:55.460 --> 00:01:56.930
could tell you similar stories
> 可以告诉你类似的故事

50
00:01:56.930 --> 00:01:59.205
about their work with
machine learning.
> 关于他们的机器学习工作。

51
00:01:59.205 --> 00:02:01.220
When you've learned
these skills,
> 当你学会了这些技能，

52
00:02:01.220 --> 00:02:04.550
I hope that you too will
find the great fun to dabble
> 我希望你也会发现这些技能很有趣

53
00:02:04.550 --> 00:02:06.590
in exciting different
applications
> 在不同的激动人心的应用中

54
00:02:06.590 --> 00:02:08.585
and maybe even
different industries.
> 甚至不同的行业。

55
00:02:08.585 --> 00:02:10.640
In fact, I find it
hard to think of
> 事实上，我发现很难想象

56
00:02:10.640 --> 00:02:12.650
any industry that
machine learning is
> 任何一个行业

57
00:02:12.650 --> 00:02:14.180
unlikely to touch in
> 不可能被机器学习触及

58
00:02:14.180 --> 00:02:17.465
a significant way now
or in the near future.
> 现在或在不久的将来。

59
00:02:17.465 --> 00:02:20.765
Looking even further
into the future,
> 甚至更进一步地展望未来，

60
00:02:20.765 --> 00:02:22.835
many people, including me,
> 许多人，包括我，

61
00:02:22.835 --> 00:02:25.310
are excited about
the AI dream of
> 对AI梦想感到兴奋

62
00:02:25.310 --> 00:02:28.480
someday building machines as
intelligent as you or me.
> 有一天制造出和你我一样聪明的机器。

63
00:02:28.480 --> 00:02:30.150
This is sometimes called
> 这有时被称为

64
00:02:30.150 --> 00:02:33.705
Artificial General
Intelligence or AGI.
> 人工通用智能或AGI。

65
00:02:33.705 --> 00:02:36.470
I think AGI has
been overhyped and
> 我认为AGI已经被过度炒作

66
00:02:36.470 --> 00:02:39.200
we're still a long way
away from that goal.
> 我们离那个目标还有很长的路要走。

67
00:02:39.200 --> 00:02:41.150
I don't know. It'll take
> 我不知道。可能需要

68
00:02:41.150 --> 00:02:44.380
50 years or 500 years
or longer to get there.
> 50年、500年或更长时间才能到达那里。

69
00:02:44.380 --> 00:02:45.994
But mostly AI researchers
> 但大多数AI研究人员

70
00:02:45.994 --> 00:02:47.960
believe that the best way to get
> 认为实现这一目标的最佳途径是

71
00:02:47.960 --> 00:02:52.040
closer toward that goal is by
using learning algorithms.
> 通过使用学习算法来更接近这个目标。

72
00:02:52.040 --> 00:02:54.200
Maybe ones that take
some inspiration
> 也许是那些受到启发

73
00:02:54.200 --> 00:02:56.015
from how the human brain works.
> 从人类大脑的工作方式。

74
00:02:56.015 --> 00:02:58.265
You also hear a
little more about
> 你还会听到更多关于

75
00:02:58.265 --> 00:03:01.640
this Quest for AGI
later in this course.
> 这个追求AGI的探索在这门课程中稍后会有更多的讨论。

76
00:03:01.640 --> 00:03:04.355
According to a
study by McKinsey,
> 根据麦肯锡的一项研究，

77
00:03:04.355 --> 00:03:07.820
AI and machine learning
is estimated to create
> 人工智能和机器学习预计将创造

78
00:03:07.820 --> 00:03:10.460
an additional 13
trillion US dollars
> 额外的13万亿美元


79
00:03:10.460 --> 00:03:13.625
of value annually
by the year 2030.
> 价值，到2030年每年创造。

80
00:03:13.625 --> 00:03:16.220
Even though machine learning
is already creating
> 尽管机器学习已经创造了

81
00:03:16.220 --> 00:03:19.370
tremendous amounts of value
in the software industry,
> 在软件行业中创造了巨大的价值，

82
00:03:19.370 --> 00:03:21.185
I think there could be
> 我认为可能会有

83
00:03:21.185 --> 00:03:23.990
even vastly greater
value that has yet to be
> 甚至更大的价值尚未被发现

84
00:03:23.990 --> 00:03:26.825
created outside the
software industry
> 在软件行业之外创造

85
00:03:26.825 --> 00:03:28.580
in sectors such as retail,
> 在零售等行业，

86
00:03:28.580 --> 00:03:29.975
travel, transportation,
> 旅行，交通，

87
00:03:29.975 --> 00:03:33.850
automotive, materials
manufacturing, and so on.
> 汽车，材料制造等等。

88
00:03:33.850 --> 00:03:37.010
Because of the massive
untapped opportunities
> 由于巨大的未开发机会

89
00:03:37.010 --> 00:03:39.155
across so many
different sectors,
> 在许多不同的行业中，

90
00:03:39.155 --> 00:03:42.230
today there is a vast
unfulfilled demand
> 今天有一个巨大的未满足的需求

91
00:03:42.230 --> 00:03:44.290
for this skill set.
> 对这种技能的需求。

92
00:03:44.290 --> 00:03:46.580
That's why this is
such a great time to
> 这就是为什么现在是

93
00:03:46.580 --> 00:03:48.925
be learning about
machine learning.
> 学习机器学习的绝佳时机。

94
00:03:48.925 --> 00:03:52.380
If you find machine learning
applications exciting,
> 如果你发现机器学习应用很有趣，

95
00:03:52.380 --> 00:03:55.685
I hope you stick with
me through this class.
> 我希望你能跟着我一起学习这门课程。

96
00:03:55.685 --> 00:03:58.130
I can almost
guarantee that you'll
> 我几乎可以保证你会

97
00:03:58.130 --> 00:04:01.060
find mastering these
skills worthwhile.
> 发现掌握这些技能是值得的。

98
00:04:01.060 --> 00:04:03.200
In the next video, we'll look at
> 在下一个视频中，我们将看一下

99
00:04:03.200 --> 00:04:07.550
a more formal definition of
what is machine learning.
> 机器学习的更正式定义。

100
00:04:07.550 --> 00:04:09.710
And we'll begin to talk about
> 我们将开始讨论

101
00:04:09.710 --> 00:04:10.850
the main types of
> 主要类型的

102
00:04:10.850 --> 00:04:13.699
machine learning
problems and algorithms.
> 机器学习问题和算法。

103
00:04:13.699 --> 00:04:15.560
You pick up some of
> 你会学到一些

104
00:04:15.560 --> 00:04:19.010
the main machine learning
terminology and start to get
> 主要的机器学习术语，并开始了解

105
00:04:19.010 --> 00:04:21.530
a sense of what are the
different algorithms
> 不同的算法是什么样的

106
00:04:21.530 --> 00:04:24.710
and when each one
might be appropriate.
> 以及何时使用每种算法是合适的。

107
00:04:24.710 --> 00:04:28.710
So let's go on to
the next video.
> 那么让我们继续下一个视频。