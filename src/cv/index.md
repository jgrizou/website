---
style: CV
navbar:
  cv: true
---

<button type="button" class="btn btn-default btn-lg pull-right" id="buttonpdf">
  <span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span> PDF
</button>

<div id="cv"></div>

<script>
$( document ).ready( function () {
    $( "#cv" ).load( "{{ "cv.html" | relative_path | web_path}}" );
});

$("#buttonpdf").click(function(){
    window.open("cv.pdf");
});

</script>
