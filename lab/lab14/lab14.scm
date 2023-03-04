

(define (compose-all funcs) 
    (lambda (x) 
        (cond ((null? funcs) x)
             (else  ((compose-all (cdr funcs)) ((car funcs) x))
             )
        )
    )
)
