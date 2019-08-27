---
layout: default
---

# Now

Research fellow [@ CRI Collaboratory](https://research.cri-paris.org) (Paris, France). I am designing a [web application to explain self-calibrating interfaces](projects/vault). Try it below or start the [challenge](projects/vault/challenge).

{% include vault_demo_quick_access.html %}

Previously, I led a team of 9 researchers in the [Cronin Group](http://www.chem.gla.ac.uk/cronin/) on the [digitization of Chemistry](projects/chemobot) and cofounded [Pollen Robotics](https://www.pollen-robotics.com/) to commercialize an innovative [modular robotic technology](https://www.luos-robotics.com/en/).

More broadly, I enjoy making things work in the real world. I devise AI algorithms, build robots, and develop web services. I bloom when leading innovative teams.


# Highlights

My favorite projects:

- [An interface that reads your mind](projects/vault)
- [Robotics and AI in a Chemistry lab](projects/chemobot)
- [Self-calibrating interfaces: an intriguing AI paradigm](projects/thesis)
- [Open source robotics](projects/open_robotics)

Worth a read:

- [Exploration of Self-Propelling Droplets Using a Curiosity Driven Robotic Assistant](https://arxiv.org/abs/1904.12635)
- [The Open Vault Challenge -- Learning how to build calibration-free interactive systems by cracking the code of a vault](https://arxiv.org/abs/1906.02485)


{% for post in site.posts offset:0 limit:1 %}
Latest blog post: <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }} ({{ post.date | date_to_string }})</a>
{% endfor %}
