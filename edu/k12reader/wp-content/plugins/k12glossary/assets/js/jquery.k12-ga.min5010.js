/*! K12Reader.com K12 Core - v1.0.0 - Generated: 20-07-2014 */
"undefined"!=typeof jQuery&&jQuery(document).ready(function(a){"use strict";var b="",c=/\.(zip|exe|dmg|pdf|doc.*|xls.*|ppt.*|mp3|txt|rar|wma|mov|avi|wmv|flv|wav)$/i;"undefined"!=a("base").attr("href")&&(b=a("base").attr("href")),a("a").on("click",function(){var d=!0,e=a(this),f="undefined"!=typeof e.attr("href")?e.attr("href"):"",g=f.match(document.domain.split(".").reverse()[1]+"."+document.domain.split(".").reverse()[0]);if(!f.match(/^javascript:/i)){var h=[];if(h.value=0,h.non_i=!1,f.match(/^mailto\:/i))h.category="email",h.action="click",h.label=f.replace(/^mailto\:/i,""),h.loc=f;else if(f.match(c)){var i=/[.]/.exec(f)?/[^.]+$/.exec(f):"undefined";h.category="download",h.action="click-"+i[0],h.label=f.replace(/ /g,"-"),h.loc=b+f}else f.match(/^https?\:/i)&&!g?(h.category="external",h.action="click",h.label=f.replace(/^https?\:\/\//i,""),h.non_i=!0,h.loc=f):f.match(/^tel\:/i)?(h.category="telephone",h.action="click",h.label=f.replace(/^tel\:/i,""),h.loc=f):d=!1;if(d&&(_gaq.push(["_trackEvent",h.category.toLowerCase(),h.action.toLowerCase(),h.label.toLowerCase(),h.value,h.non_i]),"undefined"===e.attr("target")||"_blank"!=e.attr("target").toLowerCase()))return setTimeout(function(){location.href=h.loc},400),!1}})});