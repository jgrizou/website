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
        - link: {{ "/cv" | web_path}}
          display: CV
        - link: {{ "/moocs" | web_path}}
          display: MOOCs

  - side: right
    name: contact
    link: {{ "/contact" | web_path}}
    display: Contact
---
