{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "    from Tkinter import *\n",
    "    import matplotlib.pyplot as plt\n",
    "    import numpy as np\n",
    "    import pandas as pd\n",
    "\n",
    "    def app():\n",
    "        root = Tk()\n",
    "        root.config(background='white')\n",
    "        root.geometry(\"700x700\")\n",
    "        \n",
    "        lab = Label(root, text=\"Live Plotting\", bg = 'white').pack()\n",
    "        \n",
    "        #fig = Figure()\n",
    "        \n",
    "        #ax = fig.add_subplot(111)\n",
    "        #ax.set_xlabel(\"X axis\")\n",
    "        #ax.set_ylabel(\"Y axis\")\n",
    "        #ax.grid()\n",
    "        \n",
    "        #graph = FigureCanvasTkAgg(fig, master=root)\n",
    "        #graph.get_tk_widget().pack(side=\"top\",fill='both',expand=True)\n",
    "     \n",
    "        x = np.random.randint(1, 100, 5)\n",
    "        plt.hist(x, bins=20)\n",
    "        plt.ylabel('No of times')\n",
    "        plt.show()\n",
    "\n",
    "        #def plotter():\n",
    "            #while continuePlotting:\n",
    "                #ax.cla()\n",
    "                #ax.grid()\n",
    "                #dpts = data_points()\n",
    "                #ax.plot(range(10), dpts, marker='o', color='orange')\n",
    "                #graph.draw()\n",
    "                #time.sleep(1)\n",
    "     \n",
    "        #def gui_handler():\n",
    "            #change_state()\n",
    "            #threading.Thread(target=plotter).start()\n",
    "     \n",
    "        #b = Button(root, text=\"Start / Stop\", command=gui_handler, bg=\"red\", fg=\"white\")\n",
    "        #b.pack()\n",
    "        \n",
    "        root.mainloop()\n",
    "     \n",
    "    if __name__ == '__main__':\n",
    "        app()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
