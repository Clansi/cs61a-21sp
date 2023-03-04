(define-macro (switch expr cases)
  (cons 
        (map ( ( )
                        (cons  (cdr case)))
             cases)))
