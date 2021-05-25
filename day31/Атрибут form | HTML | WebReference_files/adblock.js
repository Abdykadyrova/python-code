		var ya_hor = '<div id="yandex_rtb_R-A-330647-1"></div>' +
'<script>' +
'    (function(w, d, n, s, t) {' +
'        w[n] = w[n] || [];' +
'        w[n].push(function() {' +
'            Ya.Context.AdvManager.render({' +
'                blockId: "R-A-330647-1",' +
'                renderTo: "yandex_rtb_R-A-330647-1",' +
'                async: true' +
'            });' +
'        });' +
'        t = d.getElementsByTagName("script")[0];' +
'        s = d.createElement("script");' +
'        s.type = "text/javascript";' +
'        s.src = "//an.yandex.ru/system/context.js";' +
'        s.async = true;' +
'        t.parentNode.insertBefore(s, t);' +
'    })(this, this.document, "yandexContextAsyncCallbacks");' +
'</script>';

		var ya_ver = '<div id="yandex_rtb_R-A-330647-2"></div>' +
'<script>' +
'    (function(w, d, n, s, t) {' +
'        w[n] = w[n] || [];' +
'        w[n].push(function() {' +
'            Ya.Context.AdvManager.render({' +
'                blockId: "R-A-330647-2",' +
'                renderTo: "yandex_rtb_R-A-330647-2",' +
'                async: true' +
'            });' +
'        });' +
'        t = d.getElementsByTagName("script")[0];' +
'        s = d.createElement("script");' +
'        s.type = "text/javascript";' +
'        s.src = "//an.yandex.ru/system/context.js";' +
'        s.async = true;' +
'        t.parentNode.insertBefore(s, t);' +
'    })(this, this.document, "yandexContextAsyncCallbacks");' +
'</script>';
		
		if (document.getElementById('#block-12') && window.canRunAds === undefined) {
			document.getElementById('#block-12').prepend(ya_ver);
		}
		if (document.getElementById('#block-13') && window.canRunAds === undefined) {
			document.getElementById('#block-13').prepend(ya_ver);
		}
		if (document.getElementById('#block-16') && window.canRunAds === undefined) {
			document.getElementById('#block-16').prepend(ya_ver);
		}
		if (document.getElementById('#block-24') && window.canRunAds === undefined) {
			document.getElementById('#block-24').prepend(ya_hor);
		}
		if (document.getElementById('#block-25') && window.canRunAds === undefined) {
			document.getElementById('#block-25').prepend(ya_hor);
		}
		if (document.getElementById('#block-26') && window.canRunAds === undefined) {
			document.getElementById('#block-26').prepend(ya_hor);
		}