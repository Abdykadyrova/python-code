(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
'use strict';var f=this||self;function k(a,b){a=a.split(".");var c=f;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};(class{constructor(a,b){this.g=b===l?a:""}}).prototype.toString=function(){return this.g.toString()};var l={};var m="function"===typeof Uint8Array;function n(){}let p;function r(a,b,c){a.h=null;p&&(b||(b=p),p=null);b||(b=[]);a.o=void 0;a.j=-1;a.g=b;a:{if(b=a.g.length){--b;var d=a.g[b];if(!(null===d||"object"!=typeof d||Array.isArray(d)||m&&d instanceof Uint8Array)){a.l=b-a.j;a.i=d;break a}}a.l=Number.MAX_VALUE}a.m={};if(c)for(b=0;b<c.length;b++)d=c[b],d<a.l?(d+=a.j,a.g[d]=a.g[d]||t):(u(a),a.i[d]=a.i[d]||t)}const t=[];function u(a){let b=a.l+a.j;a.g[b]||(a.i=a.g[b]={})}
function v(a,b){if(b<a.l){b+=a.j;var c=a.g[b];return c!==t?c:a.g[b]=[]}if(a.i)return c=a.i[b],c===t?a.i[b]=[]:c}function w(a,b){a=v(a,b);return null==a?a:!!a}function x(a){a=v(a,3);return null==a?0:a}function y(a,b){a=w(a,b);return null==a?!1:a}function z(a,b,c){b<a.l?a.g[b+a.j]=c:(u(a),a.i[b]=c);return a}function A(a,b,c,d){c!==d?z(a,b,c):b<a.l?a.g[b+a.j]=null:(u(a),delete a.i[b]);return a}function B(a,b,c){a.h||(a.h={});if(!a.h[c]){let d=v(a,c);d&&(a.h[c]=new b(d))}return a.h[c]}
function C(a,b,c){a.h||(a.h={});let d=c?D(c):c;a.h[b]=c;return z(a,b,d)}function D(a){if(a.h)for(var b in a.h){var c=a.h[b];if(Array.isArray(c))for(var d=0;d<c.length;d++)c[d]&&D(c[d]);else c&&D(c)}return a.g}function E(a,b){p=b=b?JSON.parse(b):null;a=new a(b);p=null;return a}n.prototype.toString=function(){return D(this).toString()};var G=class extends n{constructor(a){super();r(this,a,F)}},F=[17];var I=class extends n{constructor(a){super();r(this,a,H)}},H=[8];var K=class extends n{constructor(a){super();r(this,a,J)}},J=[27];var M=class extends n{constructor(a){super();r(this,a,L)}},L=[1,2,3];var N=class extends n{constructor(){super();r(this,void 0,null)}};var O=class extends n{constructor(a){super();r(this,a,null)}};var Q=class extends n{constructor(a){super();r(this,a,P)}},R=class extends n{constructor(){super();r(this,void 0,null)}},P=[13];var aa=class extends n{constructor(a){super();r(this,a,null)}};var ca=class extends n{constructor(){super();r(this,void 0,ba)}},ba=[12];function S(a,b){a=a.getElementsByTagName("META");for(let c=0;c<a.length;++c)if(a[c].getAttribute("name")===b)return a[c].getAttribute("content")||"";return""};function T(a,b){b=new CustomEvent(b);a.body.dispatchEvent(b)}
var da=class{constructor(a){this.body=a;var b=S(a,"namespace");if(!b){b="ns-"+Math.random().toString(36).substr(2,5);a:{var c=a.getElementsByTagName("META");for(let d=0;d<c.length;++d)if("namespace"===c[d].getAttribute("name")&&c[d].getAttribute("index")===(0).toString()){c[d].setAttribute("content",b);break a}c=a.querySelector("#mys-meta");c||(c=document.createElement("div"),c.id="mys-meta",c.style.position="absolute",c.style.display="none",a.appendChild(c));a=document.createElement("META");a.setAttribute("name",
"namespace");a.setAttribute("content",b);a.setAttribute("index",(0).toString());c.appendChild(a)}}}addEventListener(a,b){this.body.addEventListener(a,b)}};function U(a){var b=document;a=String(a);"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());return b.createElement(a)};function V(a){if(1>=a.h.offsetWidth||1>=a.h.offsetHeight)return!1;a.g.remove();T(a.i,"spanReady");return!0}
var ea=class{constructor(a,b){this.i=a;this.j=b;this.h=U("SPAN");this.g=U("DIV");this.h.style.fontSize="6px";this.h.textContent="go";this.g.style.position="absolute";this.g.style.top="100%";this.g.style.left="100%";this.g.style.width="1px";this.g.style.height="0";this.g.style.overflow="hidden";this.g.style.visibility="hidden";this.g.appendChild(this.h)}wait(){if(!y(this.j,1)&&(T(this.i,"spanStart"),this.i.body.appendChild(this.g),!V(this)))return new Promise(a=>{const b=setInterval(()=>{V(this)&&
(clearInterval(b),a())},x(this.j))})}};var fa=class{constructor(a){this.g=a;this.contentH=this.contentW=0}};function W(a){a.h&=-31}function X(a,b){a.h|=b}var ha=class{constructor(a,b){this.g=a;this.i=b;new ca;this.h=0}execute(){}};function Y(a,b,c){if(b&&c){var d=a.g.i;d.contentW=b;d.contentH=c}b=E(M,S(a.h.body,"engine_msg")||"[]");return a.g.execute(b,void 0,void 0)||Promise.resolve()}function ia(a){var b;W(a.g);X(a.g,1);null===(b=window.AFMA_Communicator)||void 0===b?void 0:b.addEventListener("onshow",()=>{X(a.g,32)});let c=0;const d=a.h.body;d.addEventListener("browserRender",()=>{++c;if(1===c)T(a.h,"overallStart"),Y(a).then(()=>{T(a.h,"overallQuiet")});else{var g=d.clientWidth,h=d.clientHeight;g&&h&&Y(a,g,h)}})}
var ja=class{constructor(a,b,c){this.h=new da(a);this.g=c(this.h,b)}};function ka(a){a.h.length=0;a.g=!0}function Z(a,b){a.isRunning=!0;const c=()=>{a.g=!1;const d=a.h.shift();return void 0===d?(a.isRunning=!1,Promise.resolve()):Z(a,d())};return b?b.then(c,()=>{if(a.g)return c();a.isRunning=!1;return Promise.reject()}):c()}function la(a,b){for(const c of b)a.h.push(c);if(!a.isRunning)return Z(a)}var ma=class{constructor(){this.g=this.isRunning=!1;this.h=[]}};var na=class extends ha{constructor(){super(...arguments);this.j=new ma}execute(){ka(this.j);return la(this.j,[()=>{},()=>{let a;const b=B(B(this.i.g,Q,6),O,1);b&&(a=(new ea(this.g,b)).wait());T(this.g,"browserStart");T(this.g,"browserStartEnd");W(this);X(this,2);return a},()=>{T(this.g,"browserReady");T(this.g,"browserReadyEnd");X(this,4);T(this.g,"overallReady")},()=>{T(this.g,"browserQuiet");T(this.g,"browserQuietEnd");X(this,8)}])}};
(function(a){let b=null;k("mys.engine.init",(c,d)=>{c=E(aa,S(d,"render_config")||"[]");b=new ja(d,c,a);ia(b)});k("mys.engine.stage",()=>b?b.g.h:0)})(function(a,b){b=new fa(b);var c;if(null==v(b.g,6)){var d=B(b.g,K,1),g=B(b.g,I,12)||new I;var h=new R;var e=v(d,42);e=null==e?e:+e;h=A(h,1,(null==e?0:e)||1,0);w(g,18)&&A(h,2,!0,!1);w(g,19)&&A(h,3,!0,!1);e=new Q;var q=w(g,6)||!1;e=A(e,10,q,!1);q=v(g,2)||0;e=A(e,7,q,0);q=w(g,15)||!1;e=A(e,18,q,!1);h=C(e,23,h);e=v(g,20)||0;0<e&&A(h,24,e,0);e=new O;e=A(e,
3,100,0);e=A(e,4,1E4,0);w(g,4)?(A(e,6,!0,!1),A(e,7,"monospace",""),A(e,8,"IMWimw0.!?@","")):(w(g,5)&&A(e,9,!0,!1),A(e,5,!0,!1));C(h,1,e);e=new N;q=v(g,22)||"";e=A(e,3,q,"");(null===(c=B(d,G,10))||void 0===c?0:y(c,6))&&A(e,1,!0,!1);y(d,16)&&!w(g,1)&&A(e,2,!0,!1);C(h,4,e);C(b.g,6,h)}return new na(a,b)});}).call(this);
