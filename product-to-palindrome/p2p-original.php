<?php
class ProductTopPalindrome
{
    // const MAX_RANGE_END = 99999;

    protected $candidates = array(); // reverse sorted by product, factor => product
    protected $errorMessage;
    protected $iterations = 0;
    protected $palindrome;
    protected $rangeBegin;
    protected $time;

    public function calculatePalindrome($rangeEnd, $rangeBegin = null)
    {
        if (is_null($rangeBegin)) {
            $rangeBegin = 1;
        }

        $rangeBegin = (int) $rangeBegin;
        $rangeEnd   = (int) $rangeEnd;

        if (! $this->isValidRange($rangeEnd, $rangeBegin)) {
            return false;
        }

        $product = $rangeEnd * $rangeEnd;

        if (! is_int($product)) {
            $this->errorMessage = "The product $rangeEnd * $rangeEnd is too large for this machine.";
            return false;
        }

        $this->insertCandidate(array(
            'a' => $rangeEnd,
            'b' => $rangeEnd,
            'p' => $product));

        $this->rangeBegin = $rangeBegin;
        $this->time = microtime(true);

        while ($candidate = $this->getNextCandidate()) {
            $this->iterations++;

            if ($this->isPalindrome($candidate['p'])) {
                $this->palindrome = $candidate;
                break;
            }
        }

        $this->time = round((microtime(true) - $this->time), 3);

        return null;
    }

    public function getNextCandidate()
    {
        $candidate = array_shift($this->candidates);

        if (isset($candidate)) {
            $nextFactorA = $candidate['a'] - 1;

            if ($candidate['b'] == $nextFactorA and $nextFactorA >= $this->rangeBegin) {
                $this->insertCandidate(array(
                    'a' => $nextFactorA,
                    'b' => $nextFactorA,
                    'p' => $nextFactorA * $nextFactorA));
            }

            $nextFactorB = $candidate['b'] - 1;
            $product = $candidate['p'] - $candidate['a'];

            if ($product >= $candidate['a'] and $nextFactorB >= $this->rangeBegin) {
                $this->insertCandidate(array(
                    'a' => $candidate['a'],
                    'b' => $nextFactorB,
                    'p' => $product));
            }
        }

        return $candidate;
    }

    public function insertCandidate($newCandidate)
    {
        $candidates = array();

        foreach($this->candidates as $candidate) {
            if (isset($newCandidate) and $newCandidate['p'] > $candidate['p'] or $newCandidate['p'] == $candidate['p'] and $newCandidate['a'] > $candidate['a']) {
                $candidates[] = $newCandidate;
                $newCandidate = null; // mark new candidate as inserted
            }

            $candidates[] = $candidate;
        }

        if (isset($newCandidate)) {
            // new candidate not inserted yet
            $candidates[] = $newCandidate;
        }

        $this->candidates = $candidates;
    }

    public function isPalindrome($number)
    {
        $number = (string) $number;

        for ($i = 0, $j = strlen($number) - 1; $i < $j; $i++, $j--) {
            if ($number[$i] != $number[$j]) {
                return false;
            }
        }

        return true;
    }

    public function isValidRange($rangeEnd, $rangeBegin)
    {
        if ($rangeEnd < 0) {
            $this->errorMessage = 'The end of the range must be a positive non null integer.';
            return false;
        }

        if ($rangeBegin < 0 or $rangeBegin > $rangeEnd) {
            $this->errorMessage = "The begining of the range must be a positive non null integer, lower than $rangeEnd";
            return false;
        }

        return true;
    }

    public function printCandidate($candidate)
    {
        return sprintf('%d * %d = %d', $candidate['a'], $candidate['b'], $candidate['p']);
    }

    public function printReport()
    {
        return array(
            'palindrome' => isset($this->palindrome)? $this->printCandidate($this->palindrome) : 'none',
            'iterations' => $this->iterations,
            'time'       => $this->time,
            'stack'      => array_map(array($this, 'printCandidate'), $this->candidates),
            'error'      => $this->errorMessage,
        );
    }
}

$palindrome = new ProductTopPalindrome();
$palindrome->calculatePalindrome(999);
echo '<pre>';
print_r($palindrome->printReport());
