
;;https://github.com/uikit/uikit/releases/download/v3.15.23/uikit-3.15.23.zip
;; https://github.com/uikit/uikit/releases/download/v3.15.23/uikit-3.15.23.zip


(define-public javascript-uikit
  (package
    (name "javascript-uikit")
    (version "3.15.23")
    (source
      (origin
      (method url-fetch)
      (uri (string-append "https://github.com/uikit/uikit/releases/download/v"
                            version "/uikit-" version ".zip"))
      (sha256
        (base32 "0cdjwqh1pm75n9m7srsghffmxwaf87yamr2v931x5xks31iflrx7"))))
    (build-system trivial-build-system)
    (arguments
     `(#:modules ((guix build utils))
       #:builder
       (begin
         (use-modules (guix build utils))
         (let* ((out (assoc-ref %outputs "out"))
                (name "uikit")
                (unzip (string-append (assoc-ref %build-inputs "unzip")
                                      "/bin/unzip"))
                (targetdir (string-append out "/share/genenetwork2/javascript/" name))
                (source (assoc-ref %build-inputs "source")))
           (invoke unzip source)
	   (copy-recursively  "."  targetdir)))))
    (native-inputs
     `(("source" ,source)
       ("unzip" ,unzip)))
    (home-page "https://getuikit.com/")
    (synopsis "A lightweight and modular front-end framework
for developing fast and powerful web interfaces")
    (description "UIkit is a lightweight and modular front-end
framework for developing fast and powerful web interfaces.")
    (license license:bsd-3)))

