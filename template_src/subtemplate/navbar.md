---
style: Navbar
brand:
  name: Jonathan Grizou
  link: {{ "/" | web_path}}
navbar:
  - name: home
    link: {{ "/" | web_path}}
    display: Home

  - name: projects
    link: {{ "/projects" | web_path}}
    display: Projects

  - name: publications
    link: {{ "/publications" | web_path}}
    display: Publications

  - dropdown:
      display: More
      item:
        - link: http://forum.jgrizou.com/
          display: Forum
        - link: {{ "/quotes" | web_path}}
          display: Quotes
        - link: {{ "/cv" | web_path}}
          display: CV

  - side: right
    name: contact
    link: {{ "/contact" | web_path}}
    display: Contact
---
