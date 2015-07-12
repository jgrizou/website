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

  - name: cv
    link: {{ "/cv" | web_path}}
    display: CV

  - dropdown:
      display: More
      item:
        - link: {{ "/open_science" | web_path}}
          display: Open Science

  - side: right
    name: contact
    link: {{ "/contact" | web_path}}
    display: Contact
---
