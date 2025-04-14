// NOTE: This is critical! Bootstrap Flatly attaches fade to the popover element, so it must be removed manually.
//       If not removed, the fade class renders popover elements invisible.
function delayRemoveFade() {
  setTimeout($('.fade').removeClass('fade'), 300);
}

// Add ARIA live region for dynamic messages
$(document).ready(function() {
  $('body').append('<div id="aria-live-messages" class="sr-only" aria-live="polite"></div>');
});

setTimeout(function () {
  $("#save_success").addClass('fade');
  // Announce save success to screen readers
  $('#aria-live-messages').text('Changes saved successfully');
}, 2000);

function fromEditToDetail() {
  var path = window.location.pathname.replace('edit', 'detail');
  window.location.href = path;
}

function rowClick(id) {
  const activeClass = 'usa-alert usa-alert--success';
  console.log('rowclick', id);
  $("tr").removeClass(activeClass);
  const $row = $("#" + id);
  $row.addClass(activeClass);
  $("i").removeAttr('aria-disabled');
  $("i").attr('id', id);

  // Add keyboard support
  $row.attr('tabindex', '0')
      .attr('role', 'button')
      .on('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          $(this).click();
        }
      });

  // Announce selection to screen readers
  $('#aria-live-messages').text('Row ' + id + ' selected');
}

// Add keyboard navigation for interactive elements
$(document).ready(function() {
  $('[role="button"]').on('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      $(this).click();
    }
  });
});
