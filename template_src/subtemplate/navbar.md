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
      display: Drop
      item:
        - link: {{ "/" | web_path}}
          display: Test

  - side: right
    name: contact
    link: {{ "/contact" | web_path}}
    display: Contact
---
