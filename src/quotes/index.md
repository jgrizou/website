---
style: Default
---

<div class="btn-group btn-group-justified filters-button-group" role="group" aria-label="...">
<div class="btn-group" role="group">
<button type="button" class="btn btn-default" data-filter="*">
All
</button>
</div>
<div class="btn-group" role="group">
<button type="button" class="btn btn-default" data-filter=".science">
Science
</button>
</div>
<div class="btn-group" role="group">
<button type="button" class="btn btn-default" data-filter=".other">
Others
</button>
</div>
</div>

<div class="grid">


{{ {"filter": "science", "quote": "Tout ce qui existe dans l'univers est le fruit du hasard et de la nécessité.", "author": "Démocrite Apocrypha by Jacques Monod", "source": "Le Hasard et la Nécessité", "year": "1970"} | quote }}

{{ {"filter": "other", "quote": "Ever tried. Ever failed. No matter. Try again. Fail again. Fail better.", "author": "Samuel Beckett"} | quote }}

{{ {"filter": "science", "quote": "C’est bien plus la coutume et l’exemple qui nous persuade, qu’aucune connaissance certaine.", "author": "René Descartes", "source": "Discours de la methode", "year": "1637"} | quote }}

{{ {"filter": "other", "quote": "Les hommes n'ont jamais de remords des choses qu'ils sont dans l'usage de faire.", "author": "Voltaire", "source": "Dialogue du chapon et de la poularde", "year": "1763"} | quote }}

{{ {"filter": "science", "quote": "All models are wrong, but some are useful.", "author": "George Box", "year": "1970s"} | quote }}

{{ {"filter": "science", "quote": "Children have real understanding only of that which they invent themselves, and each time that we try to teach them something too quickly, we keep them from reinventing it themselves.", "author": "Jean Piaget"} | quote }}

{{ {"filter": "other", "quote": "If we wait for the moment when everything, absolutely everything is ready, we shall never begin.", "author": "Ivan Turgenev"} | quote }}

{{ {"filter": "science", "quote": "Because instruments determine what can be done, they also determine to some extent what can be thought.", "author": "Albert van Helden and Thomas Hankins", "year": "1994"} | quote }}

{{ {"filter": "science", "quote": "La recherche de la vérité doit être le but de notre activité; c’est la seule fin qui soit digne d’elle. Sans doute devons nous d’abord nous efforcer de soulager les souffrances humaines, mais pourquoi? Ne pas souffrir, c’est un idéal négatif et qui serait plus sûrement atteint par l’anéantissement du monde.", "author": "Henri Poincaré", "source": "La valeur de la science", "year": "1905"} | quote }}

{{ {"filter": "science", "quote": "We think; biological evolution does not. But when problems are very hard, thinking may not help that much. We may all be relatively blind watchmakers.", "author": "Stuart Kauffman", "source": "At Home in the Universe - p202", "year": "1995"} | quote }}

{{ {"filter": "other", "quote": "Life is not a matter of holding good cards, but of playing a poor hand well.", "author": "Robert Louis Stevenson"} | quote }}

{{ {"filter": "other", "quote": "On ne juge pas un homme sur le nombre de fois qu'il tombe, mais sur le nombre de fois qu'il se relève.", "author": "Jigoro Kano"} | quote }}

{{ {"filter": "other", "quote": "So many things are possible just as long as you don't know they're impossible.", "author": "Norton Juster"} | quote }}

{{ {"filter": "other", "quote": "We're all in this game together.", "author": "William Styron"} | quote }}

{{ {"filter": "other", "quote": "The thing that is really hard, and really amazing, is giving up on being perfect and beginning the work of becoming yourself.", "author": "Anna Quindlen"} | quote }}

{{ {"filter": "other", "quote": "Only someone who is well prepared has the opportunity to improvise.", "author": "Ingmar Bergman"} | quote }}

{{ {"filter": "other", "quote": "Learn the rules, break the rules, make up new rules, break the new rules.", "author": "Marvin Bell"} | quote }}

{{ {"filter": "other", "quote": "All you need is love. But a little chocolate now and then doesn't hurt.", "author": "Charles M. Schulz"} | quote }}

{{ {"filter": "other", "quote": "Spoon feeding in the long run teaches us nothing but the shape of the spoon.", "author": "E.M. Forster"} | quote }}

{{ {"filter": "other", "quote": "The world is indeed comic, but the joke is on mankind.", "author": "H.P. Lovecraft"} | quote }}

{{ {"filter": "other", "quote": "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are already naked. There is no reason not to follow your heart.", "author": "Steve Jobs"} | quote }}

{{ {"filter": "other", "quote": "Adults are always asking little kids what they want to be when they grow up ’cause they’re looking for ideas.", "author": "Paula Poundstone"} | quote }}

{{ {"filter": "other", "quote": "If we had no faults we should not take so much pleasure in noting those of others.", "author": "François La Rochefoucauld"} | quote }}

{{ {"filter": "other", "quote": "Make your mistakes, take your chances, look silly, but keep on going. Don’t freeze up.", "author": "Thomas Wolfe"} | quote }}

{{ {"filter": "other", "quote": "It's not denial. I'm just selective about the reality I accept.", "author": "Bill Watterson"} | quote }}


</div>

<script>
$(document).ready( function() {
  var $grid = $(".grid");
  // init Isotope
  $grid.imagesLoaded(function(){
    $grid.isotope({
      layoutMode: "packery",
      itemSelector: ".grid-item",
      packery: {
      gutter: 10
      },
    });
  });
  $(".filters-button-group").on( "click", "button", function() {
    var filterValue = $( this ).attr("data-filter");
    $grid.isotope({ filter: filterValue });
  });
});
</script>
