---
style: CV
---

<button type="button" class="btn btn-default btn-lg pull-right" id="buttonhtml">
  <span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span> HTML
</button>
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

$("#buttonhtml").click(function(){
    window.open("cv_standalone.html");
});

</script>