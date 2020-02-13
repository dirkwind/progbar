import sys, time, random

# this needs to be reworked; code is messy and redundant

class ProgressBar():

    def __init__(self, progress_string='█', void_string='░', bar_size=50, static=False):
        '''progress_string is the string that marks completed progress
        void_string is the string that marks incompleted progress
        bar_size is the length of the bar (aka the max num of void_strings and progress_strings)
        static determines whether or not the bar's progress can change without creating a new line
        '''
        self.progress_string = str(progress_string)
        self.void_string = str(void_string)
        if type(bar_size) != int:
            raise TypeError(f'bar_size must be an integer (a {type(bar_size)} was given)')
        else:
            self.bar_size = bar_size
        self.progress = 0
        if type(static) != bool:
            raise TypeError(f'static must be a boolean (a {type(static)} was given)')
        else:
            self.static = static
        self.paused = False
        self.title = ''

    def getFactor(self, percent):
        return (percent * self.bar_size // 100)

    def startProgress(self, title='none', hide = False):
        '''Starts a progress bar that remains on one line. Resets your progress to 0%'''
        if not hide: # prints bar to screen if not hidden
            if not self.static:
                sys.stdout.write(title + ' |' + (str(self.void_string) * self.bar_size) + '| 0%' + chr(8)*((self.bar_size * len(self.void_string))+5))  
            else:
                sys.stdout.write(title + ' |' + (str(self.void_string) * self.bar_size) + '| 0%\n')
            sys.stdout.flush()
        self.title = title
        self.progress = 0

    def updateProgress(self, percent=None, hide = False):
        '''Updates the progress on a started progress bar based on the percent given.'''
        factor = self.getFactor(percent)
        if not hide:
            if not self.static:
                sys.stdout.write('|' + self.progress_string * factor + (self.void_string * (self.bar_size - factor)) + '| ' + str(percent) + '% ' + chr(8)*(((self.bar_size - factor) * len(self.void_string)) + (factor * len(self.progress_string) + 5 + len(str(percent)))))
            else:
                sys.stdout.write(self.title + ': |' + self.progress_string * factor + (self.void_string * (self.bar_size - factor)) + '| ' + str(percent) + '%\n')
            sys.stdout.flush()
        self.progress = percent
        
    def endProgress(self, message='', hide = False):
        '''Ends a started progress bar. Automatically updates your bar to 100%.'''
        self.progress = 100
        if not hide:
            if not self.static and not self.paused:
                sys.stdout.write('|' + self.progress_string * self.bar_size + '| ' + str(self.progress) + '%' + '\n' + message + '\n')
            else:
                sys.stdout.write(self.title + ' |' + self.progress_string * self.bar_size + '| ' + str(self.progress) + '%' + '\n' + message + '\n')
            sys.stdout.flush()
    
    def pauseProgress(self, hide=False):
        '''Pauses a started progress bar. Unlike endProgress, this does not automatically put your bar at 100%.'''
        if not hide:
            factor = self.getFactor(self.progress)
            if not self.static:
                sys.stdout.write('|' + (self.progress_string * factor) + (self.void_string * (self.bar_size - factor)) + '| ' + str(self.progress) + '%\n')
        self.paused = True
    
    def resumeProgress(self):
        '''The same as startProgress but doesn't reset your progress to 0%'''
        if not self.static:
            factor = self.getFactor(self.progress)
            sys.stdout.write(self.title + ' |' + (self.progress_string * factor) + (self.void_string * (self.bar_size - factor)) + '| ' + str(self.progress) + '%' + chr(8)* (4 + len(str(self.progress)) + ((self.bar_size - factor) * len(self.void_string)) + (factor * len(self.progress_string))))
        sys.stdout.flush()

    def getProgress(self):
        '''Prints the current progress in bar form and isn't in one-line format.'''
        factor = self.getFactor(self.progress)
        if not self.static:
            sys.stdout.write(self.title + ' |' + (self.progress_string * factor) + (self.void_string * (self.bar_size - factor)) + '| ' + str(self.progress) + '%\n')
        sys.stdout.flush()

    def easyBar(self, title='Default', message='Default', loadingfactor=1000):
        '''A cosmetic loading bar that updates its progress based on its loadingfactor'''
        if not self.static:
            self.startProgress(title)

            for p in range(1, 101):
                self.updateProgress(p)
                time.sleep(random.randint(1, loadingfactor + 1) / 1000)

            self.endProgress(message)
    
    def __repr__(self):
        return "ProgressBar('{}', '{}', {}, {})".format(self.progress_string, self.void_string, self.bar_size, self.static)

    def __str__(self):
        self.getProgress()

    @staticmethod
    def toPercent(amount, total):
        return round((amount / total) * 100)