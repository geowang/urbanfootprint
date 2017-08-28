// ==========================================================================
// Project:   SproutCore - JavaScript Application Framework
// Copyright: ©2006-2011 Strobe Inc. and contributors.
//            ©2008-2011 Apple Inc. All rights reserved.
// License:   Licensed under MIT license (see license.js)
// ==========================================================================

// ========================================================================
// RootResponder Tests: Touch
// ========================================================================
/*global module, test, ok, equals */

var pane, view, layer, evt, evt2;

module("SC.RootResponder", {
  setup: function() {
    // Create our pane.
    pane = SC.Pane.extend({
      childViews: ['contentView'],
      contentView: SC.View.extend({
        acceptsMultitouch: YES,
        touchStart: function() {},
        touchesDragged: function() {},
        touchEnd: function() {}
      })
    });
    // (Actually create it, in a run loop.)
    SC.run(function() {
      pane = pane.create().append();
    });

    // Get our view and layer.
    view = pane.contentView;
    layer = view.get('layer');
    // Create and fill in our events.
    evt = SC.Event.simulateEvent(layer, 'touchstart', { touches: [], identifier: 4, changedTouches: [], pageX: 100, pageY: 100 });
    evt2 = SC.Event.simulateEvent(layer, 'touchstart', { touches: [], identifier: 5, changedTouches: [], pageX: 200, pageY: 200 });
    evt.changedTouches.push(evt);
    evt.changedTouches.push(evt2);
    evt2.changedTouches.push(evt);
    evt2.changedTouches.push(evt2);
  },

  teardown: function() {
    pane.destroy();
    evt = evt2 = layer = view = pane = null;
  }
});

// With v1.11, SC.Touch now provides its own velocity along each axis.
test("SC.Touch velocity", function() {
  // Get a layer
  var touch,
    lastTimestamp;

  lastTimestamp = evt.timeStamp;

  // Trigger touchstart
  SC.Event.trigger(layer, 'touchstart', [evt]);

  touch = SC.RootResponder.responder._touches[evt.identifier];

  equals(touch.velocityX, 0, "Horizontal velocity begin at zero");
  equals(touch.velocityY, 0, "Vertical velocity begin at zero");

  // Copy the last DOM touch as the basis of an updated DOM touch.
  touch = SC.copy(touch);
  touch.pageX += 100;
  touch.pageY += 100;

  evt = SC.Event.simulateEvent(layer, 'touchmove', { touches: [touch], identifier: 4, changedTouches: [touch] });
  evt.timeStamp = lastTimestamp + 100;

  SC.Event.trigger(layer, 'touchmove', [evt]);

  touch = SC.RootResponder.responder._touches[evt.identifier];

  equals(touch.velocityX, 1, 'VelocityX for 100 pixels in 100 ms is 1.');
  equals(touch.velocityY, 1, 'VelocityY for 100 pixels in 100 ms is 1.');

});

test("averagedTouchesForView", function() {
  // Start touch.
  SC.Event.trigger(layer, 'touchstart', evt);

  // Copy the last DOM touch as the basis of an updated DOM touch.
  var touch1 = SC.RootResponder.responder._touches[evt.identifier];
  var touch2 = SC.RootResponder.responder._touches[evt2.identifier];

  // Get our starting average.
  var expectedAverageX = (touch1.pageX + touch2.pageX) / 2,
    expectedAverageY = (touch1.pageY + touch2.pageY) / 2,
    startAverage = SC.clone(SC.RootResponder.responder.averagedTouchesForView(view));

  equals(startAverage.x, expectedAverageX, "averagedTouchesForView correctly returns touch location averages (x)");
  equals(startAverage.y, expectedAverageY, "averagedTouchesForView correctly returns touch location averages (y)");
  ok(startAverage.d, "averagedTouchesForView's distance measurement should ... be a nonzero number. (Pythagoras doesn't play nice with integers.)");

  // Pinch out by 50 pixels in every direction.
  touch1.pageX = 50;
  touch1.pageY = 50;
  touch2.pageX = 250;
  touch2.pageY = 250;

  var moveEvt = SC.Event.simulateEvent(layer, 'touchmove', { touches: [touch1, touch2], identifier: 6, changedTouches: [touch1, touch2] });
  SC.Event.trigger(layer, 'touchmove', moveEvt);

  // Get our post-pinch average.
  var endAverage = SC.RootResponder.responder.averagedTouchesForView(view);

  ok(startAverage.x === endAverage.x && startAverage.y === endAverage.y, 'Touches moved symmetrically, so gesture center should not have moved.');
  equals(endAverage.d, startAverage.d * 2, "Touches moved apart by 2x; gesture distance should have doubled");
});
