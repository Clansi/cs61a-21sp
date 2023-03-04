(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car(cdr(cdr s))))

(define (sign val) (cond ( (= 0 val) 0 )  ((< val 0) -1) ((> val 0) 1)   ))

(define (square x) (* x x))

(define (pow base exp)
    (cond 
        ((= base 1) 1)
        ((= exp 0) 1)
        ((even? exp)(square (pow base (/ exp 2))))
        (else (* base (square(pow base (/ (- exp 1) 2)))))))
