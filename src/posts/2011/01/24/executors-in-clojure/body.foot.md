Java has a very useful package called `java.util.concurrent`, which
contains classes and interfaces for tasks, task execution tracking,
thread-to-thread communication with blocking queues, locks,
semaphores, atomic containers and the Executors Framework. This blog
post will walk you through the concepts of the Executors Framework as
seen from Clojure.

But first a word on the relationship between Clojure and existing Java
frameworks. Clojure has been designed to make Java interop as seamless
as possible. Where Java is not broken, Clojure does not in
general((clojure.string)) add a wrapping layer.((rh-quote))

((clojure.string)): An exception is the clojure.string namespace,
which got added in Clojure 1.2.

((rh-quote)): <http://clojure-log.n01se.net/date/2010-12-02.html#17:53>

The Executors Framework provides abstractions for representing tasks,
handles to running tasks and executors as objects. In Java, general
tasks (or units of work) are contained in instances of [`Runnable`]
[Runnable] or [`Callable`] [Callable]. A task is executed by calling
its `run` and `call` method respectively. The interfaces are very
straight forward:((generics))

((generics)): When in Clojure, you can think of type parameters as
being of type Object.

[Runnable]: <http://download.oracle.com/javase/6/docs/api/java/lang/Runnable.html>
    "Javadoc for java.lang.Runnable"

[Callable]: <http://download.oracle.com/javase/6/docs/api/java/util/concurrent/Callable.html>
    "Javadoc for java.util.concurrent.Callable"

    package java.lang;
    public interface Runnable {
        void run();
    }

    package java.util.concurrent;
    public interface Callable<V> {
        V call();
    }

The difference between them is that `call` can return a value, unlike
`run` which is of type void. As you might have realized, this
abstraction is a bit similar to function objects: They are both ways
of encapsulating pieces of code as objects. Naturally, Clojure
functions implement `Runnable` and `Callable` by invoking itself with
zero arguments:

    user=> (defn demo-task []
             (println "boo!")
             123)
    #'user/demo-task
    user=> (.run demo-task)
    boo!
    nil
    user=> (.call demo-task)
    boo!
    123

Now that we have a way of describing tasks, we can explore how we can
pass them to something that can execute them. The simplest abstraction
for this is the [`Executor`] [Executor]. It has one method called
`execute` that takes a `Runnable`. When it is invoked, the `Executor`
is expected to execute the task some time in the future.

[Executor]: <http://download.oracle.com/javase/6/docs/api/java/util/concurrent/Executor.html>
    "Javadoc for java.util.concurrent.Executor"

    package java.util.concurrent;
    public interface Executor {
        void execute(Runnable command);
    }

For fun, we can now implement an `Executor` that when passed a task
creates a dedicated thread for it and runs the tasks in it:

    user=> (defn create-thread-executor []
             (reify
               java.util.concurrent.Executor
               (execute [_ task]
                 (let [f #(try
                            (task)
                            ;; return value is ignored by Thread
                            (catch Throwable e
                              ;; not much we can do here
                              (.printStackTrace e *out*)))]
                   (doto (Thread. f)
                     (.start))))))
    #'user/create-thread-executor
    user=> (alter-var-root #'*out* (constantly *out*))
    #<PrintWriter java.io.PrintWriter@16c72cc>
    user=> (def exe (create-thread-executor))
    #'user/exe
    user=> (.execute exe demo-task)
    boo!
    nil

(The `alter-var-root` line makes the current repl the default output
stream for new threads.)

There are three things that the above code does not address very well:
it doesn't tell you when the task is done, it does not provide a way
of getting back any value and it does not provide a way for the
calling code to detect a failure in the task. A much richer
abstraction is the [`ExecutionService`] [ExecutionService]. It extends
the `Executor` interface and provides methods to get a result back
from a task, submit multiple tasks at once and to gracefully shut it
down: `awaitTermination`, `invokeAll`, `invokeAny`, `isShutdown`,
`isTerminated`, `shutdown`, `shutdownNow` and `submit`. Since it
allows tasks to communicate a value back, tasks can be of type
`Callable`.

[ExecutionService]: <http://download.oracle.com/javase/6/docs/api/java/util/concurrent/ExecutionService.html>
    "Javadoc for java.util.concurrent.ExecutionService"

Along with the `ExecutorService`, another concept is introduced: the
[`Future`] [Future]. An object that implements this interface
represent a handle to a task that is queued, cancelled, being executed
or has been scheduled for execution. When you submit a task to an
`ExecutorService`, you get a `Future` back. You can use it to retrieve
its result, query whether it's done yet, or cancel it, among other
things. Its interface is as follows:

[Future]: <http://download.oracle.com/javase/6/docs/api/java/util/concurrent/Future.html>
    "Javadoc for java.util.concurrent.Future"

    package java.util.concurrent;
    public interface Future<V> {
        boolean cancel(boolean mayInterruptIfRunning);
        V get();
        V get(long timeout, TimeUnit unit);
        boolean isCancelled();
        boolean isDone();
    }

When invoking the `get` method, the call will block until the task is
done or the call times out (if a timeout was given). Clojure provides
wrapper functions (whose names begin with `future-`), for all of these
methods except for `get`. (You can still access those methods with
usual Java interop.) A call to `get` can exit in five ways:

- On sucess, it returns the result of the `call` method of the task,
  if it was a `Callable`, or `nil`, if it was a `Runnable`.
  
- If the `Future` has been cancelled, a `CancellationException` is
  thrown.
  
- If the body of the task has thrown an unhandled exception, an
  `ExecutionException` is thrown with that exception as its cause.
  
- If the thread that executed the task has been interrupted, an
  `InterruptedException` is thrown.
  
- If a timeout was given and that time has passed, a
  `TimeoutException` is thrown

In addition, the Executors Framework provides the [`Executors`]
[Executors] class, which is a colletion of static factory methods for
creating various concrete instances of `ExecutorService`. Two very
useful ones are `newFixedThreadPool` and `newCachedThreadPool`. Using
thread pools is usually a good idea, since thread creation is an
expensive operation.

[Executors]: <http://download.oracle.com/javase/6/docs/api/java/util/concurrent/Executors.html>
    "Javadoc for java.util.concurrent.Executors"

`newFixedThreadPool` solves the problem by creating a fixed number of
threads, and using them to execute the tasks. The cost for creating
new threads only occurs once, but only a fixed number of tasks can be
run at the same time. The approach of `newCachedThreadPool` is to
start with no threads and creates new ones as it needs them. If a
thread is done with its task, it will stay around for sixty seconds.
If it does not get a new task in that time, it will be deallocated.
Let's try using the first kind from Clojure:

    user=> (import 'java.util.concurrent.Executors)
    java.util.concurrent.Executors
    user=> (def pool (Executors/newFixedThreadPool 4))
    #'user/create-thread-executor
    user=> (defn sleep-print-and-double [x]
             (Thread/sleep 1000)
             (println x "done!")
             (* x 2))
    #'user/sleep-and-print
    user=> (let [tasks (for [i (range 10)]
                         #(sleep-print-and-double i))
                 futures (.invokeAll pool tasks)]
             (for [ftr futures]
               (.get ftr)))
    ;; (1 sec delay)
    0 done!
    1 done!
    3 done!
    2 done!
    ;; (1 sec delay)
    4 done!
    5 done!
    7 done!
    6 done!
    ;; (1 sec delay)
    8 done!
    9 done!
    (0 2 4 6 8 10 12 14 16 18)

Not too complicated, wasn't it? I will finish by describing a macro in
Clojure that you might have heard of: `future`. (The name itself may
be a bit unfortunate, since it only tells us that we get a `Future`
object, but not what took care of the task.) `future` takes some
expressions, wraps them up as the body of an anonymous function and
passed that function to `future-call`. In other words, `(future (foo)
(bar))` is just a more convenient way of writing `(future-call (fn []
(foo) (bar)))`.

`future-call`, the function that actually does the work, submits the
given task to one of Clojure's internal thread pools((send-off)) and
gets a `Future` back. Another object that implements both `IDeref`
(which allows you to call deref/@ on it) and `Future` will be the
actual return value. Dereferencing it will invoke the `get` method of
the `Future` from the thread pool and any call to a `Future` method on
it will be delegated to that `Future` too. All this is perhaps best
clarified with the source code itself:

((send-off)): This happens to be the same one used by the
implementation of `send-off`.

    (defn future-call [^Callable f]
      (let [fut (.submit clojure.lang.Agent/soloExecutor f)]
        (reify
         clojure.lang.IDeref
          (deref [_] (.get fut))
         java.util.concurrent.Future
          (get [_] (.get fut))
          (get [_ timeout unit] (.get fut timeout unit))
          (isCancelled [_] (.isCancelled fut))
          (isDone [_] (.isDone fut))
          (cancel [_ interrupt?] (.cancel fut interrupt?)))))

`future` provides a fairly simple standard solution for starting off
some piece of code in another thread and you are likely to come across
it. Now you know how it works under the hood.

`;; raek`
