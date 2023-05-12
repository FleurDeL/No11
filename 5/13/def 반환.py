def grumpy():
    print('I am a grumpy cat:')
    def no_n_times(n):
        print('no', n, 'times...')
        def no_m_more_times(m):
            print('... and no', m, 'times')
            for i in range(n+m):
                print('no')
        return no_m_more_times
    return no_n_times
grumpy()(4)(2)