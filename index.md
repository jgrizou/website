---
layout: default
---

# Now

Research fellow @ [CRI Collaboratory](https://research.cri-paris.org) (Paris, France). I am designing a web application to demonstrate the concept of [self-calibrating interfaces](projects/thesis). A preliminary version is [available online](http://discourse.cri-paris.org/t/introduction-to-the-open-vault-challenge/201) as a puzzle game, with more details on: [https://arxiv.org/abs/1906.02485](https://arxiv.org/abs/1906.02485).

Previously, I led a team of 9 researchers in the [Cronin Group](http://www.chem.gla.ac.uk/cronin/) on the [digitization of Chemistry](projects/chemobot) and cofounded [Pollen Robotics](https://www.pollen-robotics.com/) to commercialize an innovative [modular robotic technology](https://www.luos-robotics.com/en/).

More broadly, I enjoy making things work in the real world. I devise AI algorithms, build robots, and develop web services. I bloom when leading innovative teams.


# Highlights

My favorite projects:

- [Self-calibrating interfaces: an intriguing AI paradigm](projects/thesis)
- [Robotics and AI in a Chemistry lab](projects/chemobot)
- [Open source robotics](projects/open_robotics)

Worth a read:

- [Exploration of Self-Propelling Droplets Using a Curiosity Driven Robotic Assistant](https://arxiv.org/abs/1904.12635)
- [The Open Vault Challenge -- Learning how to build calibration-free interactive systems by cracking the code of a vault](https://arxiv.org/abs/1906.02485)


{% for post in site.posts offset:0 limit:1 %}
Latest blog post: <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }} ({{ post.date | date_to_string }})</a>
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
