In this assignment we executed a C program to display time using multithreading.
I learnt and understood the following concepts in this assignment including:
1. Firstly that, thread is a single sequence stream within a process. Its basically a lightweight process.
2. Multithreading helps in running programs more efficiently.
3. The threads share some common resources like the code, data and files. But every thread has its own register set and stack.
4. Also when we work with multiple threads there is some issue in the thread synchronization because of the shared resources of threads.
So to solve these problems we can use either semaphores or mutex.
5. Semaphores and Mutex are basically ways so that a single thread completes its job and then the next thread is allowed to do so. Semaphore
is a signalling mechanism and a thread is waiting on a semaphore can be signalled by another thread.(Its like setting and unsetting a flag)
While in Mutex it locks the part of the critical section and mutex can only be signalled by the thread which called the wait function to 
unlock it. 
6. I used mutex in the C program. It has functions which initialize the mutex, lock the mutex, unlock the mutex and destroy the mutex.
7. Pthread library in C has all the functions of threading in C.
8. Also I used the time.h header file and its datatypes like the clock_t, time_t and struct tm to display the time in hours, minutes and 
seconds.
