(defun NthElement()
(terpri)
(princ "Enter the list with parantheses:- ")
(setq listr (read))
(terpri)
(princ "The list is:- ")
(write listr)
(terpri)
(princ "Enter the value of n:-")
(setq n (read))
(terpri)
(princ "The nth element in the list is:- ")
(write (nth n listr)))

(NthElement)
