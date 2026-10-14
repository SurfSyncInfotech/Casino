/* Casino Royale - behaviour that the template did not ship with:
   toasts, form handling, grid search, saved hearts, lucky ticket, result checker. */
(function ($) {
  "use strict";

  var toastTimer;
  function toast(message, isError, html) {
    var $t = $(".site-toast");
    if (!$t.length) return;
    clearTimeout(toastTimer);
    $t.toggleClass("error", !!isError);
    if (html) $t.html(message);
    else $t.text(message);
    $t.addClass("show");
    toastTimer = setTimeout(function () {
      $t.removeClass("show");
    }, Math.max(5000, String(message).length * 70));
  }
  window.royaleToast = toast;

  function ready() {
    /* ------------------------------------------------------------------
       Forms that post to /forms/<kind>
       ------------------------------------------------------------------ */
    $("form[data-ajax-form]").on("submit", function (e) {
      e.preventDefault();
      var form = this;
      var kind = $(form).attr("data-ajax-form");
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var $btn = $(form).find("button[type=submit]").prop("disabled", true);
      var data = {};
      $(form)
        .serializeArray()
        .forEach(function (f) {
          data[f.name] = f.value;
        });
      if (data.password) {
        if (data.password.length < 8) {
          $btn.prop("disabled", false);
          toast("Please choose a password with at least 8 characters.", true);
          return;
        }
        delete data.password; // never send passwords to the demo endpoint
      }
      fetch("/forms/" + kind, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      })
        .then(function (r) {
          return r.json();
        })
        .then(function (res) {
          toast(res.message || "Thank you!", !res.ok);
          if (res.ok) {
            form.reset();
            $(form).find("select").niceSelect("update");
          }
        })
        .catch(function () {
          toast("Something went wrong. Please try again or call our concierge.", true);
        })
        .finally(function () {
          $btn.prop("disabled", false);
        });
    });

    /* Sign-in: the online portal is invitation-only (front-end demo) */
    $("form[data-signin]").on("submit", function (e) {
      e.preventDefault();
      if (!this.checkValidity()) {
        this.reportValidity();
        return;
      }
      toast(
        "Welcome back! The online member portal is opening soon. Existing members, please " +
          '<a href="https://wa.me/919890512345" target="_blank" rel="noopener">message your host on WhatsApp</a>.',
        false,
        true
      );
    });

    /* Game details: take a seat / buy-in */
    $("form[data-play-form]").on("submit", function (e) {
      e.preventDefault();
      var $f = $(this);
      var amt = parseInt(($f.find("input[name=amount]").val() || "").replace(/[^0-9]/g, ""), 10);
      var min = parseInt($f.attr("data-min"), 10) || 0;
      var max = parseInt($f.attr("data-max"), 10) || Infinity;
      if (!amt || amt < min) {
        toast("Minimum buy-in for this game is ₹" + min.toLocaleString("en-IN") + ".", true);
        return;
      }
      if (amt > max) {
        toast("Maximum buy-in for this game is ₹" + max.toLocaleString("en-IN") + ".", true);
        return;
      }
      toast(
        "Great choice! Buy-in of ₹" + amt.toLocaleString("en-IN") +
          ' noted. <a href="/sign-in">Sign in</a> or <a href="/sign-up">join now</a> to take your seat.',
        false,
        true
      );
    });

    /* Star rating in review forms */
    $(".review-game i").on("click", function () {
      var idx = $(this).index();
      $(this)
        .parent()
        .children()
        .each(function (i) {
          $(this).toggleClass("ti-star-filled", i <= idx).toggleClass("ti-star", i > idx);
        });
      $(this).closest("form").find("input[name=rating]").val(idx + 1);
    });

    /* Saved hearts */
    $(".js-save").on("click", function (e) {
      e.preventDefault();
      $(this).toggleClass("saved");
      toast($(this).hasClass("saved") ? "Saved to your favourites." : "Removed from favourites.");
    });

    /* Like buttons on comments */
    $(".comment__single-action .single").on("click", function () {
      var $b = $(this);
      var n = parseInt($b.text().replace(/[^0-9]/g, ""), 10) || 0;
      var liked = $b.toggleClass("liked").hasClass("liked");
      $b.html('<i class="ti ti-thumb-up' + (liked ? "-filled" : "") + '"></i> ' + (n + (liked ? 1 : -1)));
    });

    /* Lucky ticket */
    $(".js-buy-ticket").on("click", function () {
      var picked = $(".lucky-number.active").length;
      var joker = $(".lucky-power-number.active").length;
      if (picked < 5 || !joker) {
        toast("Pick 5 lucky numbers and 1 Joker number, press 'Add Numbers', then buy your ticket.", true);
        return;
      }
      var nums = $(".lucky-number.active")
        .map(function () {
          return $(this).text();
        })
        .get()
        .join(" - ");
      toast(
        "Ticket ready: " + nums + " | Joker " + $(".lucky-power-number").text() +
          '. <a href="/sign-in">Sign in</a> to confirm your bet.',
        false,
        true
      );
    });

    /* ------------------------------------------------------------------
       Grid search (games, live casino, tournaments) combined with the
       template's isotope category filter
       ------------------------------------------------------------------ */
    var $grid = $(".filter-wrapper");
    var $search = $(".js-grid-search");
    if ($grid.length && $search.length) {
      var term = "";
      var catSel = "*";

      function applyFilter() {
        $grid.isotope({
          filter: function () {
            var $el = $(this);
            var okCat = catSel === "*" || $el.is(catSel);
            var okTerm = !term || ($el.attr("data-search") || "").indexOf(term) !== -1;
            return okCat && okTerm;
          },
        });
        var visible = $grid.data("isotope") ? $grid.data("isotope").filteredItems.length : 1;
        $(".js-no-results").toggleClass("d-none", visible > 0);
      }

      $(".result__tab-btns ul").on("click", "button", function () {
        catSel = $(this).attr("data-filter") || "*";
        applyFilter();
      });

      $search.on("input", function () {
        term = $(this).val().toLowerCase().trim();
        applyFilter();
      });
      $search.closest("form").on("submit", function (e) {
        e.preventDefault();
      });

      var q = new URLSearchParams(window.location.search).get("q");
      if (q) {
        $search.val(q).trigger("input");
      }
    }

    /* ------------------------------------------------------------------
       Draw result checker (results page)
       ------------------------------------------------------------------ */
    $("form[data-check-form]").on("submit", function (e) {
      e.preventDefault();
      var data = JSON.parse($(this).attr("data-results") || "[]");
      var no = ($(this).find("input[name=contest]").val() || "").trim().toUpperCase();
      var mine = $(this)
        .find("input.my-number")
        .map(function () {
          return parseInt($(this).val(), 10);
        })
        .get()
        .filter(function (n) {
          return !isNaN(n);
        });
      var draw = data.filter(function (d) {
        return d.no.toUpperCase() === no;
      })[0];
      if (!draw) {
        toast("We could not find draw number " + (no || "(blank)") + ". Please check the draw number on your ticket.", true);
        return;
      }
      if (!mine.length) {
        toast("Please enter at least one of your numbers.", true);
        return;
      }
      var hits = mine.filter(function (n) {
        return draw.numbers.indexOf(n) !== -1;
      });
      if (hits.length === draw.numbers.length) {
        toast("Jackpot! All " + hits.length + " numbers match for draw " + no + ". Please contact our concierge to claim your prize.");
      } else if (hits.length) {
        toast("You matched " + hits.length + " number(s): " + hits.join(", ") + ". Check the pay table for your prize.");
      } else {
        toast("No matching numbers this time for draw " + no + ". Better luck in the next draw!");
      }
    });
  }

  $(ready);
})(jQuery);
