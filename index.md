---
layout: default
---

# Now

<!-- https://nownownow.com/about -->

My name is Jonathan Grizou, I am a research fellow @ [CRI Collaboratory](https://research.cri-paris.org) (Paris, France). I am designing a password interface robust to [shoulder surfing attacks](https://en.wikipedia.org/wiki/Shoulder_surfing_(computer_security)), and studying how users accept and interact with this new type of interface. I am experimenting writing essays for this website.

Previously, I led a team of 9 researchers in the [Cronin Group](http://www.chem.gla.ac.uk/cronin/) on the [digitization of Chemistry](projects/chemobot) and cofounded [Pollen Robotics](https://www.pollen-robotics.com/) to commercialize an innovative [modular robotic technology](https://www.luos-robotics.com/en/).

More broadly, I devise AI algorithms and build robots. I bloom when leading innovative teams.

# Highlights

My favorite projects:

- [An intriguing AI paradigm](projects/thesis)
- [Robotics and AI in a Chemistry lab](projects/chemobot)
- [Open source robotics](projects/open_robotics)


{% for post in site.posts offset:0 limit:1 %}
Latest Blog Post: <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }} ({{ post.date | date_to_string }})</a>
{% endfor %}

<!--

I experiment writing essays:

- Automating everything, what for? Cooperation over competition
- Problems I had with teaching
- Nature useless vs permaculture
- The feeling of useless actions
- Paralysis of being
- Goal-babble your life
- Trust is the fuel of a heathy society, not blockchain
- Make the invisible visible (hand washing vs putting a sleep)

-->

<!-- ---

<div align="center">
  {% for link in site.navbar-links %}
        <a href="{{ site.baseurl }}{{ link[1] }}">[{{ link[0] }}]</a>
  {% endfor %}
</div> -->
