

class NotificationEngine
  attr_accessor :from, :to, :subject, :body
  def deliver(from, to, subject, body)
    # do the emailing
  end
end

class Transaction
  attr_accessor :amount, :type, :date, :created_at
  @amount = ''
  @type = ''
  @date = ''
  @created_at = ''
end

class Account
  attr_accessor :account_number, :balance, :email
  @account_number = ''
  @balance = ''
  @email = ''
end

class FinancialReportNotificationManager
  attr_accessor :transactions, :account, :report, :notifier
  def initialize(transactions, account)
    @transactions = transactions
    @account = account
    @report = ''
    @notifier = ''
  end

  # now let's use a factory method to create the report
  def create_report!
    @report = @transactions.map {
         |t| "amount: #{t.amount} type: #{t.type} date: #{t.created_at}"
    }.join("\n")
  end

  # now let's email the report
  def send_report
    @report = create_report!
    @notifier = NotificationEngine.new()
    @notifier.deliver('reporter@example.com', @account.email, 'your report', @report)
  end
end

# main flow
account = Account.new()
account.account_number = 12345
account.balance = 20
account.email = 'joe@blow.com'

t1 = Transaction.new()
t1.amount = 10
t1.date = 'Monday'
t1.type = 'Deposit'
t1.created_at = 'Friday'

transactions = []
transactions.push(t1)

notifier = FinancialReportNotificationManager.new(transactions, account)
notifier.create_report!
notifier.send_report



