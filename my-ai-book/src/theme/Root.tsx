import React from 'react';
import type {Props} from '@theme/Root';

import ChatbotWidget from '@site/src/components/ChatbotWidget';

export default function Root({children}: Props): JSX.Element {
  return (
    <>
      {children}
      <ChatbotWidget />
    </>
  );
}


